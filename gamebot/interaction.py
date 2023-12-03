from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# url = "https://en.wikipedia.org/wiki/Main_Page"
url = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

#XPATH method works well for this one
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
# print(article_count)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Jon")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Dedman")
email = driver.find_element(By.NAME, "email")
email.send_keys("jonathandedman@hotmail.com")
submit = driver.find_element(By.TAG_NAME, "button")
submit.click()
