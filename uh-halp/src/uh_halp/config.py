import json
import os
import shutil

CONFIG_FILE = "~/.uh-config"


def reset_config(path: str = CONFIG_FILE):
    """
    Resets the config file to the template
    """
    dest = os.path.expanduser(path)

    if os.path.exists(dest):
        os.remove(dest)

    this_file = os.path.realpath(__file__)
    this_dir = os.path.dirname(this_file)
    source = f"{this_dir}/default_config.json"

    shutil.copyfile(source, dest)


def save_config(config, path: str = CONFIG_FILE):
    """
    Saves the config file
    """
    config_file = os.path.expanduser(path)
    with open(config_file, "wt") as f:
        json.dump(config, f, indent=4)


def get_config(path: str = CONFIG_FILE):
    """
    Reads the config file, creating it from template if it doesn't exist
    """
    config_file = os.path.expanduser(path)
    if not os.path.exists(config_file):
        reset_config(path)

    with open(config_file) as f:
        config = json.load(f)

    return config
