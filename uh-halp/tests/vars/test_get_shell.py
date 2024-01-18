from uh_halp.vars import get_shell


def test_get_shell(monkeypatch):
    monkeypatch.setenv("SHELL", "csh")
    assert get_shell() == "csh"


def test_get_shell_fallback(monkeypatch):
    monkeypatch.delenv("SHELL")
    monkeypatch.setenv("ComSpec", "csh")
    assert get_shell() == "csh"


def test_get_shell_long_var_name(monkeypatch):
    monkeypatch.setenv("SHELL", "/home/user/bin/custom/korne")
    assert get_shell() == "korne"


def test_get_shell_win_path(monkeypatch):
    monkeypatch.setenv("SHELL", "C:\\SYSTEM32\\COMMAND.COM")
    assert get_shell() == "COMMAND.COM"
