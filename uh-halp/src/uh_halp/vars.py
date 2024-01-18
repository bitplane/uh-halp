"""
Gets template variables that can be inserted into the context.
"""

import os
import platform
import subprocess
import sys


def get_os():
    """
    Returns a string describing the OS.
    """
    system = platform.system()
    if system == "Linux":
        try:
            return subprocess.check_output(["lsb_release", "-ds"]).decode().strip()
        except Exception:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        return line.strip().split("=")[1].strip('"')
    elif system == "Darwin":
        lines = subprocess.check_output(["sw_vers"]).decode().split("\n")
        words = [word.split(":", maxsplit=1)[-1].strip() for word in lines if word]
        return " ".join(words)
    elif system == "Windows":
        return f"Windows {platform.release()}"
    elif "BSD" in system:
        release = subprocess.check_output(["uname", "-r"]).decode().strip()
        return f"{system} {release}"

    return system


def get_shell():
    """
    Returns the user's shell executable name.
    """
    shell_cmd = os.environ.get("SHELL", os.environ.get("ComSpec", "unknown"))
    shell_cmd = shell_cmd.replace("\\", "/")
    return os.path.basename(shell_cmd)


def apply_vars(vars: dict, template: dict):
    """
    Replaces strings in a json-style object tree. Use {var}
    """
    if isinstance(template, str):
        return template.format(**vars)
    elif isinstance(template, dict):
        return {
            apply_vars(vars, key): apply_vars(vars, value)
            for key, value in template.items()
        }
    elif isinstance(template, list):
        return [apply_vars(vars, item) for item in template]
    else:
        return template


def get_vars() -> dict:
    """
    Gets variables that can be replaced with templates.
    To use one, reference it like {var} in any string field.

    Current keys are:

    - shell: The user's shell executable name.
    - os: A string describing the OS and its version.
    - query: The query string.
    - pwd: The current working directory.
    - key: the secret key for the service (blank here, requested interactively if needed)
    """
    return {
        "shell": get_shell(),
        "os": get_os(),
        "query": " ".join(sys.argv[1:]),
        "key": None,  # updated later if required
        # I'm not sending this one, you can if you want.
        "pwd": os.getcwd(),
    }
