from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.co.uk/")


driver.close()
# time.sleep(5)
# driver.quit()
