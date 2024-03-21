import os, requests
from typing import Optional, List, Literal


class IvyCheck:
    """
    The main client class for interacting with the IvyCheck API.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> None:
        """
        :param api_key: The IvyCheck API key
        :param base_url: The base URL of the IvyCheck API. Defaults to the production API.
        """

        self.base_url = base_url

        if api_key is None:
            api_key = os.getenv("IVYCHECK_API_KEY")

        if api_key is None:
            raise ValueError(
                "API_KEY is not passed and not set in the environment variables"
            )
        self.api_key = api_key

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        if base_url is None:
            if os.getenv("IVYCHECK_BASE_URL") is None:
                self.base_url = "https://api.ivycheck.com/"
            else:
                self.base_url = os.getenv("IVYCHECK_BASE_URL")
        else:
            self.base_url = base_url

        self.base_url = self.base_url.rstrip("/")

        # instantiate subclient
        self.checks = Checks(self)


class Checks:

    def __init__(self, client: IvyCheck) -> None:
        self.client = client

    def hallucination(self, text: str, context: str):
        """
        Perform a hallucination check on the given text against the specified context.

        :param text: The text to be checked for hallucinations.
        :param context: The context against which the text will be validated.
        """

        url = f"{self.client.base_url}/checks/hallucination"

        payload = {"text": text, "context": context}

        response = requests.post(url, json=payload, headers=self.client.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def pii(
        self,
        text: str,
        pii_types: List[
            Literal[
                "CREDIT_CARD",
                "EMAIL_ADDRESS",
                "IBAN_CODE",
                "IP_ADDRESS",
                "PERSON",
                "PHONE_NUMBER",
                "LOCATION",
                "ORGANIZATION",
            ]
        ] = [
            "CREDIT_CARD",
            "EMAIL_ADDRESS",
            "IBAN_CODE",
            "IP_ADDRESS",
            "PERSON",
            "PHONE_NUMBER",
        ],
        language: Literal["en", "fr", "de"] = "en",
    ):
        """
        Perform a PII check.

        :param text: The text to be checked.
        :param pii_types: A list of PII types to check for. Allowed values are "CREDIT_CARD", "EMAIL_ADDRESS",
                          "IBAN_CODE", "IP_ADDRESS", "PERSON", "PHONE_NUMBER".
        :param language: The language of the text. Allowed values are "en", "fr", "de". Defaults to "en".
        """
        url = f"{self.client.base_url}/checks/pii"
        payload = {"text": text, "pii_types": pii_types, "language": language}
        response = requests.post(url, json=payload, headers=self.client.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def prompt_injection(self, text: str):
        """
        Perform a prompt injection check.

        :param text: The text to be checked for prompt injection.
        """
        url = f"{self.client.base_url}/checks/prompt_injection"
        payload = {"text": text}
        response = requests.post(url, json=payload, headers=self.client.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text
