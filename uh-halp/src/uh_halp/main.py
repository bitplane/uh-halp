"""
Contains main entrypoint
"""

import importlib
import sys

from .config import CONFIG_FILE, get_config
from .keys import get_key
from .vars import apply_vars, get_vars


def show_help():
    """
    uh
        command line help on the command line

    Usage: uh [query]

    Example:
        user@host$ uh get the time
        date +%H:%M:%S

    config is in ~/.uh_config. Each field is parsed with mustache.
    Access tokens go in ~/.uh-keys
    """
    doc = show_help.__doc__
    halp = "\n".join((line[4:] for line in doc.split("\n")))

    print(halp)
    return 0


def main() -> int:
    """
    Entrypoint for the CLI.
    """
    needs_help = len(sys.argv) == 1 or (
        len(sys.argv) == 2 and any(halp in sys.argv[1] for halp in ("halp", "help"))
    )

    if needs_help:
        show_help()
        return 0

    config = get_config()
    current = config.get("current", None)

    if current not in config["services"]:
        choices = ", ".join(config["services"].keys())
        print(f"'{current}' is not one of: {choices}")
        print(f"edit {CONFIG_FILE}")
        return 0

    current_config = config["services"][current]
    vars = get_vars()

    key = None

    if current_config.get("use_key", False):
        key = get_key(current)
        if not key:
            print(f"{current} needs an access key.")
            return 1

    vars["key"] = key

    params = apply_vars(vars, current_config["params"])

    module = importlib.import_module(f"{current_config['module']}")
    response = module.query(**params)
    print(response)


if __name__ == "__main__":
    sys.exit(main())
