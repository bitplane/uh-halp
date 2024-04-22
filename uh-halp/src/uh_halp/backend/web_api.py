import json

import requests


def query(endpoint, method, query, post_data, headers, response_path):
    """
    Standard web API request
    """

    if isinstance(post_data, dict):
        post_data = json.dumps(post_data)

    response = requests.request(
        method, endpoint, params=query, data=post_data, headers=headers
    )

    if response_path:
        current = response.json()
        for p in response_path:
            current = current[p]
        return current
    else:
        return response.text
