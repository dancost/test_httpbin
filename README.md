# Allure report version:

  ### Requirements:
  - Windows machine
  - Python 3x is installed and added to PATH
  - Java is installed

  
  ### How to run:
  - Open PowerShell and install Scoop
  ```
  iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
  ```
  - Use Scoop to install Allure
  ```
  scoop install allure
  ```
  - Launch run_with_allure.bat
  - pray...
  
  ### run_with_allure.bat will:
  
  - Install requirements.txt
  - Run test script with --alluredir and -vv arguments
  - Open Allure report in new browser window
  
  ![allure_report](https://raw.githubusercontent.com/dancost/test_httpbin/allure/allure_report.JPG)
