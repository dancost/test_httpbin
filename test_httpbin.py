import requests


class TestGet:
    # query string to append to the get request URL
    args = "?fruits=oranges,bananas&drinks=fanta,nestea&sweets=mars,toffifee,snickers&guests=bob,alice,tom&place=home"
    tuple_args = '?fruits=("apple","banana","cherry")'
    url = "https://httpbin.org/get"

    # Define get request function.
    def get_request(self, url=url, method='GET', args=''):
        if method == 'GET':
            r = requests.get(url + args)

        elif method == 'OPTIONS':
            r = requests.options(url)

        elif method == "POST":
            r = requests.post(url, data=args)

        return r

    # 1. Check route returns 200 OK status with empty args
    def test_get_response_200(self):
        assert self.get_request(url=self.url).status_code == 200

    # 2. Check route returns 200 status with valid arguments
    def test_get_with_args(self):
        assert self.get_request(url=self.url, args=self.args).status_code == 200

    # 3. Check response args are correctly formatted
    def test_get_args_content_format(self):
        response = self.get_request(url=self.url, args=self.args).json()
        assert response['args'] == {
            "drinks": "fanta,nestea",
            "fruits": "oranges,bananas",
            "guests": "bob,alice,tom",
            "place": "home",
            "sweets": "mars,toffifee,snickers"
          }

    # 4. Check response format with tuple format arguments in request
    def test_get_with_tuple_args(self):
        response = self.get_request(url=self.url, args=self.tuple_args).json()
        assert response['args'] == {"fruits": "(\"apple\",\"banana\",\"cherry\")"}

    # 5. Check content of route allows permitted methods - get, head, options
    def test_route_allowed_methods(self):
        allowed_methods = ['GET', 'HEAD', 'OPTIONS']
        response = self.get_request(url=self.url, method='OPTIONS').headers['Allow']
        for method in allowed_methods:
            assert method in response

    # 6. Check forbidden method returns correct status code
    def test_method_not_allowed(self):
        assert self.get_request(url=self.url, method='POST').status_code == 405
