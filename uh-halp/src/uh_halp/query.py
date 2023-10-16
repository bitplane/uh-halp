import sys

import openai

from .config import get_key
from .os import get_sys_msg


def from_args(args=sys.argv[1:]):
    """
    Gets the query from command line args
    """
    return " ".join(args)


def call_api():
    """
    Calls the OpenAI API with the query from the command line.
    """
    query = from_args()
    openai.api_key = get_key()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": get_sys_msg()},
            {"role": "user", "content": query},
        ],
    )
    return response["choices"][0]["message"]["content"]


def clean(response: str):
    """
    Cleans the response from the API, because we can't trust it to play nicely.
    """
    split_response = response.split("```")
    if len(split_response) == 3:
        response = split_response[1]

    split_response = [line for line in response.split("\n") if line.strip()]
    response = split_response[0].strip() if split_response else ""

    if not response:
        return "uh, dunno. sorry :("

    return response


def query():
    """
    Queries the OpenAI API and returns the result
    """
    response = call_api()
    return clean(response)
