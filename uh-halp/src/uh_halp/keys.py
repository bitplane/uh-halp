import json
import os

KEY_FILE = "~/.uh-keys"


def prompt_key(service: str):
    key = input(f">>> Need a key for {service}, paste it here: ").strip()
    return key


def load_keys(key_file: str = KEY_FILE) -> dict:
    key_file = os.path.expanduser(key_file)

    if os.path.exists(key_file):
        with open(key_file, "rt") as f:
            return json.load(f)
    else:
        return {}


def save_keys(keys: dict, key_file: str = KEY_FILE):
    key_file = os.path.expanduser(key_file)
    with open(key_file, "wt") as f:
        json.dump(keys, f, indent=4)

    os.chmod(key_file, 0o600)


def save_key(service: str, key: str, key_file: str = KEY_FILE):
    """
    Save the service's key to disk
    """
    keys = load_keys(key_file)

    if key:
        print(f">>> Saving {service} key to {key_file}")
        keys[service] = key
    else:
        print(f">>> Removing {service} key from {key_file}")
        keys.pop(service, None)

    save_keys(keys, key_file)


def load_key(service: str, key_file: str = KEY_FILE):
    """
    Load the key from disk
    """
    keys = load_keys(key_file)

    return keys.get(service, None)


def get_key(service: str) -> str:
    """
    Loads the service's key from ~/.uh-keys, or prompts for it and saves it there.
    """
    key = load_key(service)
    if not key:
        key = prompt_key(service)
        save_key(service, key)

    return key
