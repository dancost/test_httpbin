echo Installing python prequisites
pip install -r requirements.txt

echo Running tests
py.test test_httpbin.py -vv --alluredir=./reports
allure serve .\reports\
pause