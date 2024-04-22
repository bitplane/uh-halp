"""
Generic web API functions
"""

import json

import requests


def query(
    endpoint: str,
    method: str,
    query: str,
    post_data: str,
    headers: dict[str, str],
    response_path: list[str | int],
) -> str:
    """
    Standard web API request.
    """

    if isinstance(post_data, dict):
        post_data = json.dumps(post_data)

    response = requests.request(
        method, endpoint, params=query, data=post_data, headers=headers
    )

    return extract(response, response_path)


def extract(response: requests.Response, response_path: list[str | int]) -> str:
    """
    If there's a response_path list, treat the response as JSON and the list as
    the path to the key we want. Use strings for property names, ints for list
    indices, and you can use negative indices to reference the end of a list
    (i.e. -1 for the last item.)
    """
    if not response_path:
        return response.text

    current = response.json()
    for p in response_path:
        current = current[p]
    return current
