from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import dotenv
from time import sleep
from datetime import datetime



url = "https://www.linkedin.com/home"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)


dotenv.load_dotenv()

# login

username = driver.find_element(By.NAME, "session_key")
username.send_keys(os.getenv("LOGIN"))

password = driver.find_element(By.NAME, "session_password")
password.send_keys(os.getenv("PASSWORD"))

submit = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button")
submit.click()

sleep(5)

#select jobs
jobs = driver.find_element(By.XPATH, "/html/body/div[6]/header/div/nav/ul/li[3]/a")
jobs.click()

sleep(5)

show_more = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[3]/div/div/main/div[2]/div[1]/div[1]/div/div/div/section/div[2]/a")
show_more.click()

sleep(5)
#search for python jobs - could adapt to other jobs later
search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
search.send_keys("Python Developer")

submit = driver.find_element(By.CLASS_NAME, "jobs-search-box__submit-button")

submit.click()

sleep(5)

# set experience level
experience_level = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/span/button")
experience_level.click()

intern = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[1]/label")
intern.click()
entry_level = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[2]/label")
entry_level.click()
associate_level = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label")
associate_level.click()

easy_apply = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")
easy_apply.click()

# get job details for spreadsheet:
        # job_title = driver.find_element(By.XPATH, "").text
        # company = driver.find_element(By.XPATH, "").text
        # location = driver.find_element(By.XPATH, "").text

# function to write application to csv file

# def write_to_csv(job_title, company, location, applied="yes"):
#     date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     with open("jobs.csv", "a") as file:
#     file.write("date, job title, company, location, applied\n")

#     file.write(f"{date}, {job_title}, {company}, {location} {applied}\n")

# apply for job - this will need to be a loop to apply for all jobs in list
sleep(5)
apply_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/span")
apply_button.click()

sleep(5)
try:
    submit_application = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button/span")
    submit_application.click()
except:
    review_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span")
    review_button.click()
    sleep(2)
    submit_application = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span")
    submit_application.click()
else:
    next_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
    next_button.click()
    sleep(2)
    submit_application = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span")
    submit_application.click()

sleep(5)


# sleep(2)
# next_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
# next_button.click()
# sleep(1)
# next_button.click()
# sleep(1)

# try:
#     additional_questions = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/h3")
#     if additional_questions.text == "Additional Questions":



#     # note could have a dictionary of questions and answers to loop throuh to answer questions
# except:
#     print("no additional questions")
#     pass

# move to next job in list


# driver.close()
