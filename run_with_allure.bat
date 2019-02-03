@echo off

echo Checking for Allure installation
if exist %USERPROFILE%\scoop\shims\allure.cmd echo Allure found. Skipping! & start %~dp0/batch/install_reqtxt.bat

echo Checking for Scoop installation
if not exist %USERPROFILE%\scoop\shims\scoop.cmd echo Scoop missing! & start %~dp0/batch/install_scoop
if exist %USERPROFILE%\scoop\shims\scoop.cmd echo Scoop found. Installing allure! & start %~dp0/batch/install_allure