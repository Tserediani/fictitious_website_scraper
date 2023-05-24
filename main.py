from enum import Enum, auto
from typing import Dict, List

from bs4 import BeautifulSoup
import requests
import asyncio

from common.constants import BASE_URL, FILENAME
from models.models import ExpertOrganisation
from common.exceptions import Non200StatusCodeError
from asynchronous.async_utils import async_get_emails
from data.data_utils import correct_file_extension

import pandas as pd
import os


class OutputFormat(Enum):
    CSV = auto()
    XLSX = auto()


def write_data(
    format: OutputFormat = OutputFormat.CSV, **kwargs: Dict[str, str]
) -> None:
    """Function to write data into file.\n
    Default format is CSV."""
    dataframe = pd.DataFrame([list(kwargs.values())], columns=list(kwargs.keys()))

    if format == OutputFormat.CSV:
        filename = correct_file_extension(FILENAME, ".csv")
        dataframe.to_csv(
            filename,
            header=not os.path.exists(filename),
            index=False,
            mode="a",
            sep="|",
        )
    elif format == OutputFormat.XLSX:
        filename = correct_file_extension(FILENAME, ".xlsx")
        # If the file doesn't exists just create new file and write data
        if not os.path.exists(filename):
            dataframe.to_excel(filename, index=False)
        # otherwise read existing data concatenate it into new dataframe and write into same file.
        old_dataframe = pd.read_excel(filename)
        new_dataframe = pd.concat([dataframe, old_dataframe])
        new_dataframe.to_excel(
            filename,
            index=False,
        )


def fetch_html(url: str) -> BeautifulSoup:
    """the function fetches the HTML content from a website."""
    response = requests.get(url)
    if not response.status_code == 200:
        raise Non200StatusCodeError(response.status_code, "Fetching Html failed")
    return BeautifulSoup(response.text, "lxml")


def parse_organisations(html_data: BeautifulSoup) -> tuple:
    for item in html_data.select('h3[class="header"]'):
        name = item.find("a").get_text()
        url = item.find("a").get("href")

        yield name, url


def get_total_pages(url: str) -> int:
    html_data = fetch_html(url)
    return int(
        html_data.select_one("li[class='pageInfo']").get_text().strip().split(" ")[-1]
    )


def extract_data(url):
    organisations = {}
    for item in parse_organisations(fetch_html(url=url)):
        name, organisation_url = item
        organisations[name] = organisation_url
    return organisations


def main() -> None:
    for i in range(1, get_total_pages(BASE_URL) + 1):
        current_url = BASE_URL.rsplit("=", maxsplit=1)[0] + f"={str(i)}"
        organisations = extract_data(current_url)
        emails = asyncio.run(async_get_emails(organisations.values()))
        for i, (name, url) in enumerate(organisations.items()):
            write_data(
                **ExpertOrganisation(name=name, emails=emails[i], url=url).dict()
            )


if __name__ == "__main__":
    main()
