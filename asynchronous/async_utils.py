from bs4 import BeautifulSoup
import httpx
import asyncio

from typing import List


async def async_fetch_html(client: httpx.AsyncClient, url: str) -> BeautifulSoup:
    response = await client.get(url)
    return BeautifulSoup(response.text, "lxml")


async def parse_organisation_emails(html_data: BeautifulSoup) -> list:
    emails = []
    email_links = html_data.select("a[title='Napísať e-mail']")
    for email_link in email_links:
        email = email_link.get_text()
        emails.append(email)

    return emails


async def async_get_emails(urls: List[str]):
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in urls:
            html_data = await async_fetch_html(client, url)
            tasks.append(parse_organisation_emails(html_data))
        return await asyncio.gather(*tasks)
