@echo off
powershell Set-ExecutionPolicy RemoteSigned -scope CurrentUser
echo Using scoop to install allure
scoop install allure
start install_reqtxt.bat