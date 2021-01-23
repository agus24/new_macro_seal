import requests

user_list = [
    {
        "username": "yohanesyoshua",
        "password": "faisal",
        "password_bank": "1111"
    }
]

def get_cookies(username, password):
    url = "https://seal-gladius.com/login"
    data = {
        "username": username,
        "password": password,
        "is_ajax": 1
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.cookies

    return None

def get_item_list():
    data = []
    cookies = get_cookies(user_list[0]['username'], user_list[0]['password'])

    url = "https://seal-gladius.com/itemmall-dataa"
    response = requests.post(url, data={"page": 1, "jenis": 7}, cookies=cookies).content.decode("utf-8")

    texts = response.split("<td>")
    texts.pop(0)

    for i, text in enumerate(texts):
        print(text[:9])
        if text[:9] == "<img src=":
            del texts[i]

    i = 0
    while i < len(texts):
        pass
    print(texts)


def send_discord_message(message):
    url = "https://discordapp.com/api/webhooks/802558967310057504/DltylKMUlMd0XevzX3NPh1ItQAmLjEmJRPRxvwz2ue9-Xo83Ct58HTVUc0nZCzVU9HQK"
    requests.post(url, data={'content': message})

get_item_list()

# def fetch_output():
#     data = []
#     tes = string.split('<td>')
#     tes.splice(0, 1)
#     for(let i = 0 ; i < tes.length ; i++) {
#         if(tes[i].indexOf("<img src=") >=0) {
#             tes.splice(i, 1)
#         }
#     }
#     for(let i = 0 ; i < tes.length ; i++) {
#         if(tes[i].indexOf("<img src=") >=0) {
#             tes.splice(i, 1)
#         }
#     }
#     for(let i = 0 ; i < tes.length ; i+=2) {
#         tes[i] = tes[i].split("</td>")[0]
#         tes[i+1] = tes[i+1].split("</td>")[0]
#         let output = {
#             name : tes[i].split("</td>")[0],
#             stok : parseInt(tes[i+1].split("</td>")[0])
#         }
#         data.push(output)
#     }
#     let outputString = '\n'
#     for(let i = 0 ; i < data.length ; i++) {
#         outputString += data[i].name + " : " + data[i].stok + "\n"
#     }
#     return new discord.RichEmbed({
#         title : "List Restok",
#         description : outputString
#     })
#     return outputString