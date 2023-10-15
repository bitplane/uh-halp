import os


def prompt_and_save():
    key = input("Need an OpenAI key, it'll be saved to ~/.uh-key: ").strip()
    save(key)
    return key


def save(key: str):
    key_path = os.path.expanduser("~/.uh-key")

    with open(key_path, "w") as f:
        f.write(key)

    os.chmod(key_path, 0o600)


def load():
    key_path = os.path.expanduser("~/.uh-key")

    try:
        with open(key_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def try_load():
    key = load()
    if not key:
        key = prompt_and_save()
    return key
