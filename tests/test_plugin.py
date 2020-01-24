import os.path
import subprocess
import sys


def test_useless_suppression():
    args = [
        sys.executable,
        "-m",
        "pylint",
        "--disable=all",
        "--enable=F",  # Disable everything except fatal errors like a non-existing file
        "--enable=useless-suppression",
        os.path.join(os.path.dirname(__file__), "examples", "useless_suppression.py"),
    ]
    # Redirect stderr in stdout to have the whole output in stdout
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # Message is present and the exit code is zero
    assert "useless-suppression" in result.stdout.decode()
    assert not result.returncode

    result = subprocess.run(
        args + ["--load-plugins=pylint_strict_informational"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    # Message is present and the exit code isn't zero
    assert "useless-suppression" in result.stdout.decode()
    assert result.returncode
