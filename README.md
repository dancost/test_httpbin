# test_httpbin:

### Task:

- The website below is a simple request-response service:
https://httpbin.org/

- Please go to the following link: https://httpbin.org/get

- Make a short description of the functionality of this endpoint 
- Play around with 'args' section and create  3-4 automated test cases using python+pytest 

### ‘/get’ endpoint functionality:

The ‘/get’ endpoint returns accepted headers in json format ("Accept", "Accept-Endcoding", "Accept-Language" etc).
It also returns 'args' data in multidictionary format via json response.

Request methods allowed on this route are  ```GET```, ```OPTIONS``` and ```HEAD```.

When performing a ```GET``` request, without a query string, the ‘/get’ route returns a json response, containing an empty dictionary and the classic request headers (```Accept```, ```Cache-control```,```User-Agent``` etc).

When performing a ```GET``` request on the ‘/get’ route and adding an optional query string – e.g “?test=spam,eggs” – to the requests parameters, the route will return a json response, containing the same request headers as above, but this time with the ‘args’ dictionary populated with data, sorted in a multidictionary format – a collection of key-value pairs, where a key can have multiple values and can occur more than once in the same container.


![get request](https://raw.githubusercontent.com/dancost/test_httpbin/master/get.JPG)


# Test Cases:

- [Can be found in test_httpbin.py](https://github.com/dancost/test_httpbin/blob/master/test_httpbin.py)
1. Check route returns 200 OK status with empty args (also checks for valid SSL cert)
2. Check route returns 200 status with valid arguments
3. Check response args are correctly formatted
4. Check response format, with tuple format arguments in request, is valid
5. Check route allows permitted methods - get, head, options
6. Check forbidden method returns correct status code

![test_pass](https://github.com/dancost/test_httpbin/blob/master/test_pass.JPG)


# Requirements:

```sh
pip install requests
pip install pytest
```

# How to run:
```py.test -vv```
or 
```pytest test_httpbin.py -vv```
