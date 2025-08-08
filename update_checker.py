import os
import requests
import yaml
from dotenv import load_dotenv

load_dotenv()

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
ENDC = "\033[0m"


def get_github_releases(repo_owner, repo_name):
    """Fetches release data from the GitHub API."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
    headers = {}
    if "GITHUB_TOKEN" in os.environ:
        headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error fetching releases for {repo_owner}/{repo_name}: {e}{ENDC}")
        return None


def get_latest_releases(releases):
    """Finds the latest stable and pre-release from a list of releases."""
    latest_release = None
    latest_prerelease = None

    for release in releases:
        if release.get("prerelease"):
            if not latest_prerelease:
                latest_prerelease = release
        else:
            if not latest_release:
                latest_release = release

        if latest_release and latest_prerelease:
            break

    return latest_release, latest_prerelease


def check_for_updates(packages_file="packages.yaml"):
    """Checks for updates for packages listed in the YAML file and prints a summary."""
    if not os.path.exists(packages_file):
        print(f"{RED}Error: '{packages_file}' not found.{ENDC}")
        return

    with open(packages_file, "r") as f:
        packages = yaml.safe_load(f)

    print("Checking for package updates...")

    update_summary = []

    for package, current_version in packages.items():
        repo_owner, repo_name = package.split("/")

        releases = get_github_releases(repo_owner, repo_name)
        if not releases:
            update_summary.append(
                {"package": package, "status": "error", "current": current_version}
            )
            continue

        latest_release, latest_prerelease = get_latest_releases(releases)

        info = {"package": package, "current": current_version}

        if latest_release:
            latest_version = latest_release["tag_name"]
            if latest_version != current_version:
                info["status"] = "update_available"
                info["latest"] = latest_version
            else:
                info["status"] = "up_to_date"
        else:
            info["status"] = "no_release"

        if latest_prerelease:
            prerelease_version = latest_prerelease["tag_name"]
            if prerelease_version != current_version and (
                not latest_release or prerelease_version != latest_release["tag_name"]
            ):
                info["prerelease"] = prerelease_version

        update_summary.append(info)

    print("\n--- Update Summary ---")
    for info in update_summary:
        package_name = info["package"]
        current_ver = info["current"]

        if info.get("status") == "update_available":
            latest_ver = info["latest"]
            print(
                f"{YELLOW}{package_name}: {current_ver} -> {latest_ver}{ENDC}", end=""
            )
            if "prerelease" in info:
                prerelease_ver = info["prerelease"]
                print(f" (Pre-release: {prerelease_ver})")
            else:
                print()
        elif info.get("status") == "up_to_date":
            print(f"{GREEN}{package_name}: {current_ver} (Up to date){ENDC}", end="")
            if "prerelease" in info:
                prerelease_ver = info["prerelease"]
                print(f" (Pre-release: {prerelease_ver})")
            else:
                print()
        elif info.get("status") == "no_release":
            print(
                f"{RED}{package_name}: {current_ver} (No stable release found){ENDC}",
                end="",
            )
            if "prerelease" in info:
                prerelease_ver = info["prerelease"]
                print(f" (Pre-release: {prerelease_ver})")
            else:
                print()
        elif info.get("status") == "error":
            print(f"{RED}{package_name}: Error checking for updates{ENDC}")


if __name__ == "__main__":
    check_for_updates()
