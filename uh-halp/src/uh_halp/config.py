import os

CONFIG_FILE = "~/.uh-config"
KEY_FILE = "~/.uh-key"


def prompt_key():
    key = input(">>> Need an OpenAI key, paste it here: ").strip()
    return key


def save_key(key: str, key_file=KEY_FILE):
    """
    Save the OpenAI key to disk
    """
    key_path = os.path.expanduser(key_file)
    print(f">>> Saving key to {key_file}")

    with open(key_path, "w") as f:
        f.write(key)

    os.chmod(key_path, 0o600)


def load_key(key_file=KEY_FILE):
    """
    Load the OpenAI key from disk
    """
    key_path = os.path.expanduser(key_file)

    try:
        with open(key_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def get_key():
    """
    Loads the OpenAI key from ~/.uh-key, or prompts for it and saves it there.
    """
    key = load_key()
    if not key:
        key = prompt_key()
        save_key(key)
    return key
