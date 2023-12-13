import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Change this values and url
numberOfVotes = 50
randomIntervalBegin = 3
randomIntervalEnd = 180
url = "https://your.url.com"

for votes in range(numberOfVotes):
  votes = votes + 1 # Fix the number of votes to not start with 0
  randomIntervalClick = random.randint(randomIntervalBegin, randomIntervalEnd) # Get a random value between two others
  print(randomIntervalClick)
  time.sleep(randomIntervalClick) # Await this random interval
  driver = webdriver.Chrome() # Open chrome
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
  buttonSelector = "i5" # You may need to change this value
  button = driver.find_element(By.ID, buttonSelector) # Find the button element by its ID selector
  button.click() # Click on the element. After every selected element, usually, you need to add to call click().

  randomAwaitValue = random.randint(3, 6) # Generate another random small value to wait before selecting the next element
  time.sleep(randomAwaitValue) # Await this random interval

  submitButtonSelector = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div' # You may also need to change this value
  button = driver.find_element(By.XPATH, submitButtonSelector) # Find the submit button by its XPATH selector
  button.click() # Click the submit button

  print("Votes: ", votes)

  time.sleep(1)
  driver.quit() # Close the browser window
