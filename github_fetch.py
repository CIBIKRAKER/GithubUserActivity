import json
import os
from urllib.request import urlopen


class GitHubFetch:
    
    def __init__(self, username):
        self.username = username
        

    def get_repo_info(self):
        url = f"https://api.github.com/users/{self.username}/events"
        response = urlopen(url)

        data_json = json.loads(response.read())

        with open("data.json", "w") as json_file:
            json.dump(data_json, json_file, indent=4)

        print("Data fetched and saved to data.json")