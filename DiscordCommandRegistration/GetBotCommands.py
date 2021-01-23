import requests
import os

url = "https://discord.com/api/v8/applications/{}/commands".format(os.environ["CLIENT_ID"])

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot " + os.environ["TOKEN"]
}

r = requests.get(url, headers=headers)
print(r.text)