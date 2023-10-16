# 05-10-2023
# Write by Laterealuz

import json
import random
import threading
import time
from datetime import datetime

import requests

_USERAGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
]

_USER_AGENT_INDEX = 1
_TIMEOUT = 20

def getCSRFToken():

    url = "https://server.com/site/api/CsrfToken/GenerateCSRFToken"

    myHeaders = headersList = {
        "Accept": "*/*",
        "User-Agent": _USERAGENT[_USER_AGENT_INDEX],
        "Content-Type": "application/json"
    }

    response = requests.get(url,  headers=myHeaders,  timeout=_TIMEOUT)
    
    if response.status_code == 200:	          
        # Get CSRF https://en.wikipedia.org/wiki/Cross-site_request_forgery
        x_xsrf_token = response.cookies["X-XSRF-TOKEN"].replace("'", "", 10)
        xsrf_token = response.cookies["XSRF-TOKEN"].replace("'", "", 10)
        xsrf = response.cookies["XSRF"].replace("'", "", 10)        
        jsonData = response.json()
        # GET JWT Token 
        token = jsonData['token']
        print("URL -->"+url)        
    else:
        print("Error ---->"+url)

    return token, x_xsrf_token, xsrf_token, xsrf
    
    
def login(token, x_xsrf_token, xsrf_token, xsrf):
    # create cookie with token CSRF in order to Add into Header
    cookie = "X-XSRF-TOKEN="+x_xsrf_token+";"
    cookie = cookie + "XSRF="+xsrf+";"
    cookie = cookie + "XSRF-TOKEN="+xsrf_token+""

    url = "https://server.com/site/api/login"

    headers = {
        'Authorization': 'Bearer '+token,
        'Content-Type': 'application/json',
        "User-Agent": _USERAGENT[_USER_AGENT_INDEX],
        'Cookie': cookie
    }

     
    data = {"login": "AENIMA", "pwd": "A123B4546B456*"}
    dataPost = json.dumps(data)
    response = requests.post(url, dataPost, headers=headers,  timeout=_TIMEOUT)
    
    if response.status_code == 200:
        dataResponse = response.text
        jsonData = response.json()
        token = jsonData['TOKEN']
        print("URL -->"+url)
    else:
        print("Error "+response.reason +" StatusCode "+str(response.status_code))
    return token
   
if __name__ == "__main__":
    token, x_xsrf_token, xsrf_token, xsrf = getCSRFToken()
    token = login(token, x_xsrf_token, xsrf_token, xsrf)
        
