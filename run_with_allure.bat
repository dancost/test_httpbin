@echo off
echo Installing scoop
powershell -nop -c "iex (new-object net.webclient).downloadstring('https://get.scoop.sh')"
echo Checking for Allure installation
if exist %USERPROFILE%\scoop\shims\allure.cmd echo Allure installed. Skipping! & goto hasScoop 


echo Using scoop to install allure
scoop install allure


:hasScoop
@echo off
echo Installing python prequisites
pip install -r requirements.txt
echo Running tests
py.test test_httpbin.py -vv --alluredir=./reports
allure serve .\reports\
pause