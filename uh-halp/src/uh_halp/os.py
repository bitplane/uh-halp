import os
import platform
import subprocess

SYS_MSG = """Input is from the command line. Answer the question with a one-line script or list of paths, not natural language. Assume pwd by default. Output is to console, no formatting."""


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
    return os.path.basename(shell_cmd)


def info():
    """
    Returns the OS info string that's used as the system message.
    """
    shell = get_shell()
    os_info = get_os()
    return f"The user is using {shell} on {os_info}"


def get_sys_msg():
    """
    Returns the system message sent to the LLM, asking it nicely to return a program.
    """
    return SYS_MSG + " " + info()
