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
