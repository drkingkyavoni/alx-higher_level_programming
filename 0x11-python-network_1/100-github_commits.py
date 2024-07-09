#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id"""

from sys import argv

from requests import get

if __name__ == "__main__":
    c_url = f"https://api.github.com/repos/{argv[1]}/{argv[2]}/commits"
    with get(c_url) as resp:
        for result in resp.json()[:10]:
            print(
                "{}: {}".format(
                    result.get("sha"), result.get("commit").get("author").get("name")
                )
            )
