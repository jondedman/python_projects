from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
import dotenv

# search_term = input("What job are you searching for? ")
search_term = "java"
url = "https://www.linkedin.com/home"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)


dotenv.load_dotenv()

# logins - this could be refactored into a function
username = driver.find_element(By.NAME, "session_key")
username.send_keys(os.getenv("LOGIN"))

password = driver.find_element(By.NAME, "session_password")
password.send_keys(os.getenv("PASSWORD"))

submit = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button")
submit.click()

sleep(20)

#select jobs from menu - could be a function

jobs = driver.find_element(By.XPATH, "/html/body/div[6]/header/div/nav/ul/li[3]/a")
jobs.click()

# expand jobs menu
sleep(2)
try:
    show_more = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[3]/div/div/main/div[2]/div[1]/div[1]/div/div/div/section/div[2]/a")
    show_more.click()
except:
    pass

#search for jobs - could adapt to a user input later - and be refactored into a function
sleep(5)
search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")


search.send_keys(search_term)

sleep(2)
try:
    submit = driver.find_element(By.CLASS_NAME, "jobs-search-box__submit-button")
    submit.click()
except:
    search.send_keys(Keys.RETURN)

sleep(5)

# set experience level - could be a function, could be made more robust by having CSS selectors and then relative XPATH before using absolute XPATHS
# experience_level = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/span/button")
# experience_level.click()

# intern = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[1]/label")
# intern.click()
# entry_level = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[2]/label")
# entry_level.click()
# associate_level = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label")
# associate_level.click()

easy_apply = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[8]/div/button")
easy_apply.click()

sleep(2)


sleep(2)
first_job = driver.find_element(By.CLASS_NAME, "job-card-container__link")
first_job.click()

sleep(2)
apply_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/span")
try:
    apply_button.click()
except:
    print("not easy apply")

sleep(2)

next_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
next_button.click()
sleep(2)
next_button.click()
sleep(2)
form = driver.find_element(By.CSS_SELECTOR, 'form')
question_labels = form.find_elements(By.CSS_SELECTOR, "label")
for label in question_labels:
    print(f'label text {label.text}')
    # if label.text == "Yes":
    #     label.find_element(By.CSS_SELECTOR, "input").click()
# print("form groups")
# form_groups = form.find_elements(By.CLASS_NAME, "jobs-easy-apply-form-section__group")
# print(len(form_groups))
# for group in form_groups:

#     print(group.__dict__)
#     print(group.text)
# print("searching just for groups")
# groups = driver.find_elements(By.CLASS_NAME, "jobs-easy-apply-form-section__group")
# print(len(groups))
# for group in groups:
#     print(group.__dict__)
#     print(group.text)

print("searching for legends")
legends = driver.find_elements(By.TAG_NAME, "legend")
print(len(legends))
for legend in legends:
    print("legend text")
    print(repr(legend.text))
    print(legend)
    print("-------------------------")
    # print(repr(legend.text))
    # find the radio input with the label text Yes
    sleep(2)
    if legend.text == "Do you have a valid driver's license?\nDo you have a valid driver's license?":
        print("found driver's license")
        yes = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='Yes']")
        no = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='No']")
    if legend.text == "Are you willing to undergo a background check, in accordance with local law/regulations?\nAre you willing to undergo a background check, in accordance with local law/regulations?\nRequired":
        print("found background check")
        yes = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='Yes']")
        no = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='No']")
        yes.click()
    if legend.text == "Will you now or in the future require sponsorship for employment visa status?\nWill you now or in the future require sponsorship for employment visa status?\nRequired":
        print("found sponsorship")
        yes = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='Yes']")
        no = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='No']")
        no.click()
    if legend.text == "Have you completed the following level of education: Bachelor's Degree?\nHave you completed the following level of education: Bachelor's Degree?\nRequired":
        print("found degree")
        yes = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='Yes']")
        no = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='No']")
        no.click()
    if legend.text == "Are you legally authorized to work in United Kingdom?\nAre you legally authorized to work in United Kingdom?\nRequired":
        yes = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='Yes']")
        no = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='No']")
        no.click()
    if legend.text == "Are you comfortable commuting to this job's location?\nAre you comfortable commuting to this job's location?\nRequired":
        print("found commute")
        yes = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='Yes']")
        no = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='No']")
        no.click()



    # print(legend.__dict__)
    # print(legend.text)
    # if label.text == "What is your first name?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Software Engineer")
    # if label.text == "What is your current company name?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Company")
    # if label.text == "What is your current job location?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("City, State")
    # if label.text == "What is your current job start date?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Jan 2019")
    # if label.text == "What is your current job end date?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Jan 2020")
    # if label.text == "What is your highest level of education?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Bachelors")
    # if label.text == "What is your graduation date?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Jan 2019")
    # if label.text == "What is your school name?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("School")
    # if label.text == "What is your degree or area of study?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Computer Science")
    # if label.text == "What is your major?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Computer Science")
    # if label.text == "What is your minor?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Computer Science")
    # if label.text == "What is your GPA?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("4.0")
    # if label.text == "What is your school location?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("City, State")
    # if label.text == "What is your school start date?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Jan 2019")
    # if label.text == "What is your school end date?":
    #     label.find_element(By.CSS_SELECTOR, "input").send_keys("Jan 2020")
    # if label.text == "What is your school start date?":
