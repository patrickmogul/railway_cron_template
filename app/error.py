import requests
import os

def notify():
    url = os.environ['NOTIFY_URL']
    # Custom Error Message
    message = "Error!"
    response = requests.post(url, data=message)
    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print("Error sending notification")

if __name__ == "__main__":
    notify()