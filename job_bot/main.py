from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import os
import dotenv
from time import sleep
from datetime import datetime
import json

# search_term = input("What job are you searching for? ")
search_term = "software engineer"
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

sleep(15)

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

sleep(2)

# Could use further try and except blocks to use CSS selectors first. The steps might need further seperating into try except blockss
def close():
    '''Closes popups'''
    print("close")
    try:
        close_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
        close_button.click()
        sleep(2)
        save_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[2]")
        save_button.click()
        sleep(2)
        final_close_button = driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div/button")
        final_close_button.click()
    except:
        pass

def load_questions():
    '''Loads the additional questions json into a dictionary'''
    print("load questions")
    try:
        with open("all_questions.json", "r") as file:
            # Check if the file is empty
            if file.read().strip():
                # If the file is not empty, seek to the beginning and load the JSON
                file.seek(0)
                all_questions = json.load(file)
            else:
                # If the file is empty, return an empty dictionary
                all_questions = {}
    except FileNotFoundError:
        all_questions = {}
    return all_questions


def extract_questions():
    '''extracts questions from the job info'''
    questions = []
    print("extract questions")
    # Find all question labels in the form
    sleep(2)
    try:
        form = driver.find_element(By.CSS_SELECTOR, 'form')
        print("form found")
        print(f'form: {form}')
        # Find all label elements within the form
    except NoSuchElementException:
        print("No form found")
        return questions
    else:
        try:
            sleep(5)
            question_labels = form.find_elements(By.CSS_SELECTOR, ".artdeco-text-input--label")
            print(f'question labels: {question_labels}')
    # iterates over the labels and adds questions to a list.
            sleep(2)
            print("line 134")


                # print(f'label: {label.text}')

            return question_labels
        except NoSuchElementException:
            try:
                question_labels = form.find_elements(By.CSS_SELECTOR, ".fb-dash-form-element__label")
                print(f'question labels: {question_labels}')
        # Now you can iterate over the labels and do something with each one
                sleep(2)
                for label in question_labels:
                    print(f'label: {label.text}')
                # questions = list(set(' '.join(label.text.lower().replace('\n', ' ').split())[:len(label.text)//2] for label in question_labels))
                questions = [label.text.replace('\n', ' ') for label in question_labels]
                print(f'questions: {questions}')
                return question_labels
            except NoSuchElementException:
                print("no questions found")
                return questions

def extract_legend_questions():
    legend_questions = []
    legends = driver.find_elements(By.TAG_NAME, "legend")
    print(f'legends: {legends}')
    for legend in legends:
        if legend.text != "":
            print(f'legend: {legend.text}')
            legend_questions.append(legend.text)
    return legend_questions



def save_questions(questions, all_questions, legend_questions):
    '''Saves new questions encountered to a local json. Takes a list of questions (from extract questions functions) and compares
    to a local copy of the additional questions json (from the load questions function)'''
    print("save questions")
    questions.extend(legend_questions)
    for question in questions:
        if question not in all_questions:
            all_questions[question] = ""
            close()
        else:
            print("question already in dictionary")
            # close()
    # Save the data
    with open("all_questions.json", "w") as file:
        json.dump(all_questions, file)

def find_inputs(type):
    print("find inputs")
    fields = driver.find_elements(By.XPATH, f"//form//input[@type='{type}']")
    for field in fields:
        label = field.find_element_by_xpath("./preceding-sibling::label")
        print(f"Question: {label.text}")
        print(f"Input HTML: {field.get_attribute('outerHTML')}")
    return fields

def answer_radio_buttons(all_questions):
    print("answer radio buttons")
    legends = driver.find_elements(By.TAG_NAME, "legend")
    print(all_questions["Do you have a valid driver's license?\nDo you have a valid driver's license?\nRequired"])
    for legend in legends:
        print(f'legend: {legend.text}')
        print("-------------------------")
        print("test")
        if legend.text != "" and legend.text in all_questions:
            print(f'all questions: {all_questions[legend.text]}')

        if legend.text != "" and legend.text in all_questions:
            yes = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='Yes']")
            no = legend.find_element(By.XPATH, "../div/label[@data-test-text-selectable-option__label='No']")
            if all_questions[legend.text] == "Yes":
                yes.click()
            elif all_questions[legend.text] == "No":
                no.click()
            else:
                print("no answer found")
        else:
            print("no legend found")


def answer_questions(all_questions):
    '''Takes a dictionary of questions and answers and attempts to find matching input fields for each question and
    attempts to fill them in.'''
    print("answer questions")
    form = driver.find_element(By.CSS_SELECTOR, 'form')
    question_labels = [(label, label.get_attribute('for')) for label in form.find_elements(By.CSS_SELECTOR, 'label')]
    print(f'question labels: {question_labels}')
    for label, label_for in question_labels:
                print(f'label: {label.text}')
                label_for = label.get_attribute('for')
                print(f'label for: {label_for}')

                try:
                    print("trying to find input")
                    input_field = driver.find_element(By.ID, label_for)
                    print(f'Question: {label.text}')
                    print(f'Input HTML: {input_field.get_attribute("outerHTML")}')
                    if input_field.get_attribute("value") == "":
                        try:
                            if input_field.get_attribute("value") != all_questions[label.text]:
                                print("trying to fill in input")
                                # input_field.send_keys("")
                                input_field.send_keys(all_questions[label.text])
                        except KeyError:
                            print("no answer found")

                    else:
                        print("input already filled in")


                except NoSuchElementException:
                    print("no input found")

                # try:
                #     print("trying to find textarea")
                #     sleep(2)
                #     textarea = driver.find_element(By.ID, label_for)
                #     answer = all_questions.get(label.text)
                #     if answer is not None:
                #         textarea.send_keys(answer)
                #     else:
                #         print(f"No answer found for label {label.text}")
                # except NoSuchElementException:
                #     print("no textarea found")


                # try:
                #     print("trying to find select")
                #     select_element = driver.find_element(By.ID, label_for)
                #     if select_element.tag_name == "select":
                #         select = Select(select_element)
                #         answer = all_questions.get(label.text)
                #         if answer is not None:
                #             print(f"Selecting option: {answer}")
                #             select.select_by_visible_text(answer)
                #         else:
                #             print(f"No answer found for label {label.text}")
                #     else:
                #         print("element is not a select")
                # except NoSuchElementException:
                #     print("no select found")

    answer_radio_buttons(all_questions)
                # try:
                #     print("trying to find radio button")
                #     sleep(2)
                #     option_text = all_questions[label.text]
                #     radio_button = driver.find_element(By.CSS_SELECTOR, f'input[data-test-text-selectable-option__input="{option_text}"]')
                #     radio_button.click()
                # except NoSuchElementException:
                #     print("no radio button found")






# This function needs to have the answering of questions refactored into a new function.
def additional_questions():
    '''Main function to trigger the checking of additional questions. First checks if additional questions are present
    then calls extract_questions, then calls save_questions if there are new questions. Then tries to find matching input fields for each question and
    attempts to fill them in. returns whether there are additional questions or not'''
    print("additional questions called")
    try:
        additional_questions = driver.find_element(By.CSS_SELECTOR, "h3.t-16.t-bold")
        print(f'additional questions: {additional_questions.text}')
        # this can be exapnded to include other questions later. for now it just checks if there are any additional questions and if so, breaks the loop
        if additional_questions.text == "Additional Questions" or additional_questions.text == "Voluntary self identification":
            # loop through questions and check dictionary for answers
            all_questions = load_questions()
            print(f'all questions: {all_questions}')
            question_labels = extract_questions()
            print(f'question labels: {question_labels}')
            legend_questions = extract_legend_questions()
            print(f'legend questions: {legend_questions}')
            questions = [label.text for label in question_labels]
            print(f'questions: {questions}')
            # if there are no questions method returns no questions to apply function.
            if len(questions) == 0:
                close()
                print("no questions found with those selectors")
                return False
            print(f'questions: {questions}')
            save_questions(questions, all_questions, legend_questions)
            answer_questions(all_questions)
            return True
            # text_inputs = find_inputs("text")
            # print(f'text inputs: {text_inputs}')
            # question_labels = form.find_elements(By.CSS_SELECTOR, ".artdeco-text-input--label")
            # print(f'question labels: {question_labels}')
            # Loop to attempt to fill in additional questions with answers from the json.

    except NoSuchElementException:
        print("no additional questions")
        return False

# should probably seperate the clicking of buttons functionality out of this function
def apply():
    '''cycles through each job, trying to press various buttons in a loop. Also, triggers additional questions'''
    try:
        apply_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button/span")
        apply_button.click()
        sleep(2)
        applied = "no"
    except NoSuchElementException:
        print("no apply button")
        applied = "yes"
        return applied
    while applied == "no":
            print("try block of apply function")
            additional_questions() #could use this to break the loop if additional questions for a simpler solution
            # this can be exapnded to include other questions later. for now it just checks if there are any additional questions and if so, breaks the loop
            # At the moment, the aboe will return True or false, but i am not sure how to use those values. once the function returns true or false it will simply try to click a buttong again before calling additional questions again on the next iterations of the loop
            try:
                print("trying to find review button")
                sleep(2)
                review_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span")
                if review_button.is_displayed():
                    review_button.click()
                    print("review button clicked")
                    sleep(2)
                    form = driver.find_element(By.CSS_SELECTOR, 'form')
                    validation_errors = form.find_elements(By.CLASS_NAME, 'artdeco-inline-feedback__message')  # Replace with the actual class name
                    if validation_errors:
                        print("Validation errors appeared")
                        close()  # Replace with your actual close function
                    else:
                        print("No validation errors appeared")
                        continue
            except NoSuchElementException:
                pass
            try:
                print("trying to find next button")
                sleep(2)
                next_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button")
                if next_button.is_displayed():
                    next_button.click()
                    print("next button clicked")
                    sleep(2)
                    continue
            except NoSuchElementException:
                pass
            try:
                print("trying to find submit application")
                sleep(2)
                # submit_application = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button")
                submit_application = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
                print(f'submit application: {submit_application}')
                if submit_application.is_displayed():
                    submit_application.click()
                    print("submit application clicked")
                    applied = "yes"
                    print("applied")
                    sleep(2)
                    # close()
                    continue
            except NoSuchElementException:
                pass
        # except NoSuchElementException:
        #     pass

            finally:
                print("finally block of apply function")
                # sleep(2)
                # close_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/button")
                # close_button.click()
                # print("close button")
                # save_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[3]/button[2]")
                # save_button.click()
                # print("save button")
                # sleep(2)
                close()
                return applied

    return applied


def write_to_csv(applied, role="not found", co="not found", location="not found", job_details="not_found", about_job="not found"):
    '''tracks which jobs have been applied for and writes the job info to a csv file'''
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("jobs.csv", "a") as file:
        file.write(f"{date}, {job_title}, {company}, {location}, {job_details}, {applied}\n")

# scroll down to load page - might no be needed.
scrollable_div = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[1]")
scrollable_div.click()

# The below probably needs to be in a function
jobs_list = []
while True:  # keep looping until we break
    old_length = len(jobs_list)
    jobs_list = driver.find_elements(By.CLASS_NAME, "job-card-container__link")
    if len(jobs_list) == old_length:  # break the loop if the number of jobs didn't increase
        break
    for _ in range(20):  # scroll down 3 times
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
        sleep(0.2)
    sleep(5)  # wait for the page to load new jobs

print(len(jobs_list))
for job in jobs_list:
    # this is the loop to click on each job in the list, then apply, then save details to csv file,
    sleep(1)
    job.click()
    sleep(2)
    try:
        job_title_element = driver.find_element(By.CSS_SELECTOR, "h2.t-24.t-bold.job-details-jobs-unified-top-card__job-title")
        job_title = job_title_element.text
        print(f'job title: {job_title}')
    except NoSuchElementException:
        job_title = driver.find_element(By.XPATH, '//*[@id="ember636"]/h2')
        print(f'job title: {job_title}')
    sleep(2)
    try:
        company = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__primary-description-container a").text
        print(f'company: {company}')
    except NoSuchElementException:
        try:
            company = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div/a')
            print(f'company: {company}')
        except NoSuchElementException:
            pass

    conditions = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/ul/li[1]/span/span[2]/span/span[1]")
    # print(f'conditions: {role}')
    location = conditions.text
    print(f'location: {location}')
    sleep(2)
    details = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/ul/li[1]")
    job_details = details.text.replace(",", " ").split("Matches")[0]
    print(f'job details: {job_details}')
    # print(job.text)
    applied = apply()
    print(f'applied: {applied}')
    write_to_csv(applied, job_title, company, location, job_details)
    sleep(5)
    # possibly another try block to close anything else that pops up before moving to next job


# can refactor to inclde the more robust solution below
# def find_element(driver, id=None, css_selector=None, xpath=None):
#     try:
#         if id:
#             return driver.find_element(By.ID, id)
#     except NoSuchElementException:
#         pass

#     try:
#         if css_selector:
#             return driver.find_element(By.CSS_SELECTOR, css_selector)
#     except NoSuchElementException:
#         pass

#     if xpath:
#         return driver.find_element(By.XPATH, xpath)  # If the element is not found, this will raise a NoSuchElementException

# # Example usage:
# element = find_element(driver, id="element-id", css_selector=".element-class", xpath="//div[@class='element-class']")
