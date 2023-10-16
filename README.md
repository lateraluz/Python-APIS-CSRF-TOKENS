# Python-APIS-CSRF-TOKENS
How to consume APIs and dealing with CSRF Tokens.

In order to consume a API that use CSRF tokens validation.

1. Get CSRF tokens (X-XSRF-TOKEN,XSRF-TOKEN,XSRF) from cookies after consuming the API.
```
   response = requests.get(url,  headers=myHeaders,  timeout=_TIMEOUT)
   x_xsrf_token = response.cookies["X-XSRF-TOKEN"].replace("'", "", 10)
   xsrf_token = response.cookies["XSRF-TOKEN"].replace("'", "", 10)
   xsrf = response.cookies["XSRF"].replace("'", "", 10)    
```  
3. Post to Login with HTTP "Cookie" header with all the tokens got them from point 1.
 ```
   cookie = "X-XSRF-TOKEN="+x_xsrf_token+";"
   cookie = cookie + "XSRF="+xsrf+";"
   cookie = cookie + "XSRF-TOKEN="+xsrf_token+""
   headers = {
        'Authorization': 'Bearer '+token,
        'Content-Type': 'application/json',
        "User-Agent": _USERAGENT[_USER_AGENT_INDEX],
        'Cookie': cookie
    }
```

## License
Feel free to improve it!

<BR>
  <BR>
**knowledge belongs to humanity**, *Pascal*
