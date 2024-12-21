import json
from urllib import request, error
from packaging.version import parse


def check_for_update(current_version: str):
    """Checks if a new version of TerminalAlert is available on PyPI."""
    try:
        url = "https://pypi.org/pypi/TerminalAlert/json"
        with request.urlopen(url, timeout=5) as response:
            data = json.load(response)
            latest_version = data["info"]["version"]

        if parse(latest_version) > parse(current_version):
            print(f"Update available: v{latest_version}. You're on v{current_version}.")
            print("Run `pip install --upgrade TerminalAlert` to update.")
        else:
            print(f"You're on the latest version: v{current_version}.")

    except error.URLError as e:
        print(f"Unable to check for updates: {e}")
