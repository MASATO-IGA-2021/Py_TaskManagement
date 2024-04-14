import requests
import json

class lineUtil:

    def __init__(self):
        file_path = "./json/information.json"
        json_file = open(file_path,"r")
        json_load = json.load(json_file)
        self.access_token = json_load["line_information"]["access_token"]
        self.user_id = json_load["line_information"]["user_id"]
        
    def send_message(self, message):
        url = "https://api.line.me/v2/bot/message/push"
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "Content-Type": "application/json"
        }
        data = {
            "to": self.user_id,
            "messages": [
                {
                    "type": "text",
                    "text": message
                }
            ]
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("Message sent successfully")
        else:
            print("Failed to send message. Status code:", response.status_code)
            


