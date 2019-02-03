@echo off
powershell Set-ExecutionPolicy RemoteSigned -scope CurrentUser


if exist %USERPROFILE%\scoop\shims\allure.cmd start %~dp0\batch\install_reqtxt.bat & exit

if not exist %USERPROFILE%\scoop\shims\scoop.cmd start %~dp0\batch\install_scoop.bat & exit

if not exist %USERPROFILE%\scoop\shims\allure.cmd start %~dp0\batch\install_allure.bat & exit


