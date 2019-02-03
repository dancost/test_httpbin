@echo off
powershell Set-ExecutionPolicy RemoteSigned -scope CurrentUser
echo Installing scoop
powershell -nop -c "iex(new-object net.webclient).downloadstring('https://get.scoop.sh')"
if not exist %USERPROFILE%\scoop\shims\allure.cmd start %~dp0\install_allure.bat & exit


