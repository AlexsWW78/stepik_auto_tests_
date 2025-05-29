from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

x_elem = browser.find_element(By.ID, "input_value")
x = x_elem.text
y = calc(x)

area_elem = browser.find_element(By.ID, "answer")
area_elem.send_keys(y)

button_submit = browser.find_element(By.ID, "solve")
button_submit.click()
