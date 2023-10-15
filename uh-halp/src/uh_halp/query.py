import sys

import openai

from .key import try_load
from .os import get_sys_msg


def from_args(args=sys.argv[1:]):
    return " ".join(args)


def query():
    query = from_args()
    openai.api_key = try_load()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": get_sys_msg()},
            {"role": "user", "content": query},
        ],
    )
    return response["choices"][0]["message"]["content"]
