from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# url = "https://en.wikipedia.org/wiki/Main_Page"
url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

money = driver.find_element(By.ID, "money").text
cookie = driver.find_element(By.ID, "cookie")

def cookie_click():
    for n in range(500):
        try:
            wait = WebDriverWait(driver, 1)
            cookie = wait.until(EC.element_to_be_clickable((By.ID, 'cookie')))
            cookie.click()
        except Exception as e:
            print(f"Error clicking cookie: {e}")

cookie_click()


cursor = driver.find_element(By.ID, "buyCursor")
cursor_cost = cursor.text.split("\n")[0].split("-")[1].strip().replace(",", "")
print(cursor_cost)
grandma = driver.find_element(By.ID, "buyGrandma")
grandma_cost = grandma.text.split("\n")[0].split("-")[1].strip().replace(",", "")
print(grandma_cost)
factory = driver.find_element(By.ID, "buyFactory")
factory_cost = factory.text.split("\n")[0].split("-")[1].strip().replace(",", "")
print(factory_cost)
mine = driver.find_element(By.ID, "buyMine")
mine_cost = mine.text.split("\n")[0].split("-")[1].strip().replace(",", "")
print(mine_cost)
shipment = driver.find_element(By.ID, "buyShipment")
shipment_cost = shipment.text.split("\n")[0].split("-")[1].strip().replace(",", "")
print(shipment_cost)
alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
alchemy_lab_cost = alchemy_lab.text.split("\n")[0].split("-")[1].strip().replace(",", "")
print(alchemy_lab_cost)
portal = driver.find_element(By.ID, "buyPortal")
portal_cost = portal.text.split("\n")[0].split("-")[1].strip().replace(",", "")
print(portal_cost)
time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
time_machine_cost = time_machine.text.split("\n")[0].split("-")[1].strip().replace(",", "")
print(time_machine_cost)


def check_element_exists(id):
    elements = driver.find_elements(By.ID, id)
    return len(elements) > 0





while int(money) < 500000000:
    money = driver.find_element(By.ID, "money").text.replace(",", "")
    try:
        if int(money) > int(time_machine_cost) and check_element_exists("buyTime machine"):
            driver.find_element(By.ID, "buyTime machine").click()
        elif int(money) > int(portal_cost) and check_element_exists("buyPortal"):
            driver.find_element(By.ID, "buyPortal").click()
        elif int(money) > int(alchemy_lab_cost) and check_element_exists("buyAlchemy lab"):
            driver.find_element(By.ID, "buyAlchemy lab").click()
        elif int(money) > int(shipment_cost) and check_element_exists("buyShipment"):
            driver.find_element(By.ID, "buyShipment").click()
        elif int(money) > int(mine_cost) and check_element_exists("buyMine"):
            driver.find_element(By.ID, "buyMine").click()
        elif int(money) > int(factory_cost) and check_element_exists("buyFactory"):
            driver.find_element(By.ID, "buyFactory").click()
        elif int(money) > int(grandma_cost) and check_element_exists("buyGrandma"):
            driver.find_element(By.ID, "buyGrandma").click()
        elif int(money) > int(cursor_cost) and check_element_exists("buyCursor"):
            driver.find_element(By.ID, "buyCursor").click()
        else:
            cookie_click()
    except (StaleElementReferenceException, NoSuchElementException) as e:
        cookie_click()




driver.quit()
