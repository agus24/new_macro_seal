from datetime import datetime
import requests


def send_message(message):
    URL = "https://discordapp.com/api/webhooks/802486083295379467/x0D2eX1Nqk4_50ugiFGvimGVjblH6QEscfKSJca46PVIftRXA3IpgNN1o6re2VDPPrpF"
    requests.post(URL, data={'content': message})

user_id = "faisaltempa"
time = datetime.now().strftime("%Y-%m-%d %H:%M")

while True:
    text = input("Mau ngomong apa? ")
    send_message(text)
# send_message(f"@everyone \n**ITEM PECAH!!** \nid : {user_id}\nIgn: \ntgl jam : {time}\n item: \nkronologi: lupa atb")
