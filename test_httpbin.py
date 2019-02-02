import requests


# query string to append to the get request URL
args = "?fruits=oranges,bananas&drinks=fanta,nestea&sweets=mars,toffifee,snickers&guests=bob,alice,tom&place=home"
tuple_args = '?fruits=("apple","banana","cherry")'
url = "https://httpbin.org/get"


# define get request function.
def get_request(url, method = 'GET', args=''):
    if method == 'GET':
        r = requests.get(url + args)

    elif method == 'OPTIONS':
        r = requests.options(url)

    elif method == "POST":
        r = requests.post(url, data=args)

    return r


# 1 check route returns 200 OK status with empty args
def test_get_response_200():
    assert get_request(url=url).status_code == 200


# 2 check route returns 200 status with valid arguments
def test_get_with_args(args=args):
    assert get_request(url=url, args=args).status_code == 200


# 3 check reponse args are correctly formatted
def test_get_args_content_format(args=args):
    response = get_request(url=url, args=args).json()
    assert response['args'] == {
        "drinks": "fanta,nestea",
        "fruits": "oranges,bananas",
        "guests": "bob,alice,tom",
        "place": "home",
        "sweets": "mars,toffifee,snickers"
      }


# 4 check response format with tuple format arguments in request
def test_get_with_tuple_args(args=tuple_args):
    response = get_request(url=url, args=args).json()
    assert response['args'] == {"fruits": "(\"apple\",\"banana\",\"cherry\")"}


# 5 Check content of route only allowes permited methods - get, head, options
def test_route_allowed_methods():
    allowed_methods = ['GET', 'HEAD', 'OPTIONS']
    response = get_request(url=url, method='OPTIONS').headers['Allow']
    for method in allowed_methods:
        assert method in response


# 6 Check forbidden method returns correct status code
def test_method_not_allowed():
    assert get_request(url=url, method = 'POST').status_code == 405
