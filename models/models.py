from pydantic import BaseModel, validator
from typing import Optional
from enum import Enum, auto

from typing import Dict, List

from common.constants import BASE_DOMAIN
from data.data_utils import clean_text

from common.exceptions import InvalidEmailException

import re


class ExpertOrganisation(BaseModel):
    base_domain: str = BASE_DOMAIN
    name: str
    emails: Optional[List[str]]
    url: str

    @validator("name")
    def validate_name(cls, name):
        cleaned_name = clean_text(name)
        return cleaned_name

    @validator("emails")
    def validate_email(cls, emails):
        email_pattern = re.compile(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        )
        cleaned_emails = []
        for email in emails:
            email_exists = re.search(email_pattern, email)
            if not email_exists:
                raise InvalidEmailException(
                    email=email, message="Invalid email address"
                )
            cleaned_emails.append(email_exists.group())
        return cleaned_emails
