# GitHub User Activity CLI

Fetch and display a GitHub user's recent activity in the terminal using the GitHub API.

---

## Features

- Fetch latest GitHub events for a specified username.
- Display common events in the terminal:
  - **PushEvent** → shows repo pushed to
  - **CreateEvent** → shows repos created
  - **WatchEvent** → shows repos starred
  - **IssuesEvent** → shows opened/closed/reopened issues
  - **PullRequestEvent** → shows opened/closed/reopened pull requests
- Saves the raw JSON data to `data.json`.
- Handles missing data gracefully.

---

## Requirements

- Python 3.6+
- No external libraries needed

---

## Usage

Run from the terminal:


python main.py <github-username>
## Example:

    python main.py CIBIKRAKER

## Output example:

Data fetched and saved to data.json
- Pushed to octocat/Hello-World
- Opened a new issue in octocat/Hello-World
- Starred octocat/Spoon-Knife
- Closed pull request #5 in octocat/Hello-World

