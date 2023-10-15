import os
import platform
import subprocess

SYS_MSG = """Input is from the command line. Answer the question with a one-line script or list of paths, not natural language. Assume pwd by default. Output is to console, no formatting."""


def get_os_info():
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
        return subprocess.check_output(["sw_vers", "-productVersion"]).decode().strip()
    elif system == "Windows":
        return f"Windows {platform.release()}"
    return "unknown"


def info():
    shell = os.environ.get("SHELL", os.environ.get("ComSpec", "unknown"))
    os_info = get_os_info()
    return f"The user is using {os.path.basename(shell)} on {os_info}"


def get_sys_msg():
    return SYS_MSG + " " + info()
