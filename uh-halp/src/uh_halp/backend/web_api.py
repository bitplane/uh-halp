import json

import requests


def query(endpoint, method, query, post_data, headers):
    """
    Standard web API request
    """

    if isinstance(post_data, dict):
        post_data = json.dumps(post_data)

    response = requests.request(
        method, endpoint, params=query, data=post_data, headers=headers
    )
    return response.text
