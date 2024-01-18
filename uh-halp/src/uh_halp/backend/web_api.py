import requests


def query(endpoint, method, query, post_data, headers):
    """
    Standard web API request
    """
    response = requests.request(
        method, endpoint, query=query, data=post_data, headers=headers
    )
    return response.text()
