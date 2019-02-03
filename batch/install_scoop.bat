@echo off
powershell Set-ExecutionPolicy RemoteSigned -scope CurrentUser
echo Installing scoop
powershell -nop -c "iex (new-object net.webclient).downloadstring('https://get.scoop.sh')"
start install_allure.bat