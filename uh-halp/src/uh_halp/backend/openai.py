"""
For calling the OpenAI completion model.
"""

import openai

from .util import clean


def query(model: str, system_prompt: str, user_prompt: str, key: str) -> str:
    """
    Calls the OpenAI API with the query from the command line.
    """
    openai.api_key = key

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
    except openai.error.AuthenticationError:
        raise Exception(
            "OpenAI key doesn't work. You might need to delete it from ~/.uh-keys"
        )

    response = response["choices"][0]["message"]["content"]
    return clean(response)
