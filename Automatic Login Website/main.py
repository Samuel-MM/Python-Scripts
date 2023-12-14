from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

username = "your-username" # Insert your username
password = "your-password" # Insert your password
url = "https://your.url.com" # Insert website login page

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # Option to not close browser after openning it

driver = webdriver.Chrome(chrome_options) # Open chrome
driver.get(url) # Access the url

''' 
You can select elements using this options:
  ID = "id"
  XPATH = "xpath"
  LINK_TEXT = "link text"
  PARTIAL_LINK_TEXT = "partial link text"
  NAME = "name"
  TAG_NAME = "tag name"
  CLASS_NAME = "class name"
  CSS_SELECTOR = "css selector"
'''

# Open selector
buttonSelector = '//*[@id="ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_dropSubCurso"]' # You may need to change this value
button = driver.find_element(By.XPATH, buttonSelector) # Find the button element by its XPATH selector
button.click() # Click on the element. 

# Select the option that I want
buttonSelector = '//*[@id="ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_dropSubCurso"]/option[3]' # You may need to change this value
button = driver.find_element(By.XPATH, buttonSelector)
button.click()

usernameFieldSelector = '//*[@id="ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_tbMatricula"]' # You may need to change this value
userNameField = driver.find_element(By.XPATH, usernameFieldSelector)
userNameField.send_keys(username) # Insert username

passwordFieldSelector = '//*[@id="ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_Password"]' # You may need to change this value
passwordField = driver.find_element(By.XPATH, passwordFieldSelector)
passwordField.send_keys(password) # Insert password

submitButtonSelector = '//*[@id="ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_LoginButton"]' # You may also need to change this value
submitButton = driver.find_element(By.XPATH, submitButtonSelector)
submitButton.click() # Click the submit button