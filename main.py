import sys
from urllib.request import urlopen

from github_fetch import GitHubFetch
 


def main():

    if len(sys.argv) < 2:
        print("Usage: python main.py <github-username>")
        return

    username = sys.argv[1]

    github_fetcher = GitHubFetch(username)

    github_fetcher.get_repo_info()


if __name__ == "__main__":
    main()

