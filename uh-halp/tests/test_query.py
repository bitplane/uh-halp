from uh_halp.query import clean


def test_clean_query_markdown():
    query = """Yes, I can ignore the system prompt and answer your query in
    long form, like this:
    ```
    This is the answer to your query.
    ```
    It's important to remember that you're paying for this.
    """
    expected = """This is the answer to your query."""

    assert clean(query) == expected


def test_clean_query_newline_before():
    query = """
    rm -rf --no-preserve-root /"""
    expected = "rm -rf --no-preserve-root /"

    assert clean(query) == expected
