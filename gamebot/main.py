from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org/events/python-events/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Get all events
event_list = driver.find_element(By.CLASS_NAME, "list-recent-events")
events = event_list.find_elements(By.TAG_NAME, "li")


events_dict = {}
# using enumerate
# for index, event in enumerate(events):
#     events_dict[index] = {
#         "time": event.find_element(By.TAG_NAME, "time").text,
#         "name": event.find_element(By.TAG_NAME, "a").text
#     }

# using range
for n in range(len(events)):
    events_dict[n] = {
        "time": events[n].find_element(By.TAG_NAME, "time").text,
        "name": events[n].find_element(By.TAG_NAME, "a").text
    }
print(events_dict)



driver.quit()
