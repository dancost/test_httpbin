@echo off
echo Using scoop to install allure
scoop install allure
start %~dp0\install_reqtxt.bat & exit

