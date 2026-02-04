from requests import get, RequestException
from json import JSONDecodeError
from src.devicemanagement.constants import Version

Nugget_Repo = "leminlimez/Nugget/releases/latest"

last_fetched_version: str = None

def is_update_available(version: str, build: int) -> bool:
    # check github for if version < tag (or == tag but build > 0)
    latest_version = get_latest_version()
    if latest_version != None:
        if build > 0 and latest_version == version: # on beta version when there is a public release
            return True
        elif Version(latest_version) > Version(version):
            return True
    return False

def get_latest_version() -> str:
    global last_fetched_version
    # get the cached version
    if last_fetched_version != None:
        return last_fetched_version
    # fetch with web requests
    try:
        response = get(f"https://api.github.com/repos/{Nugget_Repo}")
        response.raise_for_status()  # To raise an exception for 4xx/5xx responses

        data = response.json()  # Parse the JSON response

        # Check if "tag_name" exists in the response and compare the version
        tag_name = data.get("tag_name")
        if tag_name:
            last_fetched_version = tag_name.replace("v", "")  # Remove 'v' from tag_name
            return last_fetched_version
    except RequestException as e:
        print(f"Error fetching data: {e}")
    except JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    return None