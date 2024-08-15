import requests

def send_message(text):
    url = f"https://api.telegram.org/bot7394659463:AAFsaEx--gv4PKigCo_IV9zn9sBnBee0LPI/sendMessage"
    params = {"chat_id": '5439200363', "text" : text}
    response = requests.post(url, data=params)
    return response.json()