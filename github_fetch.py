import json
import os
from urllib.request import urlopen


class GitHubFetch:
    
    def __init__(self, username):
        self.username = username
        

    def get_repo_info(self):
        try:
            url = f"https://api.github.com/users/{self.username}/events"
            response = urlopen(url)
        except ValueError:
            print("Invalid URL")
            return
        try:
            data_json = json.loads(response.read())

            with open("data.json", "w") as json_file:
                json.dump(data_json, json_file, indent=4)

            print("Data fetched and saved to data.json")
        except ValueError:
            print("Error parsing JSON data")
            return

        for event in data_json:
            try:
                eventType = event["type"]
                

                if eventType == "PushEvent":
                    repoName = event["repo"]["name"]
                    print(f"- Pushed to {repoName}")
                    
                elif eventType == "CreateEvent":
                    repoName = event["repo"]["name"]
                    print(f"- Created the Repo {repoName}")
                elif eventType == "WatchEvent":
                    repoName = event["repo"]["name"]
                    print(f"- Starred {repoName}")
                elif eventType == "IssuesEvent":
                    repoName = event["repo"]["name"]
                    action = event["payload"]["action"]
                    if action == "opened":
                        print(f"- Opened a new issue in {repoName}")
                    elif action =="closed":
                        print(f"- Closed a new issue in {repoName}")
                    elif action =="reopened":
                        print(f"- Reopened a new issue in {repoName}")
                elif eventType == "PullRequestEvent":
                    repoName = event["repo"]["name"]
                    action = event["payload"]["action"]
                    pr_number = event["payload"]["number"]
                
                    if action == "opened":
                        print(f"- Opened pull request #{pr_number} in {repoName}")
                    elif action == "closed":
                        print(f"- Closed pull request #{pr_number} in {repoName}")
                    elif action == "reopened":
                        print(f"- Reopened pull request #{pr_number} in {repoName}")
            except KeyError as e:
                print(f"Missing expected data: {e}")
                continue
        
        