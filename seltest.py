from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from win32con import META_DELETEOBJECT

chrome_options = Options()
#the detach prevent the windows close
chrome_options.add_experimental_option("detach",True)
#the browser will not close on --headless code,
#CHROME_OPTIONS.add_argument("--headless")  # Runs Chrome in headless mode.
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)



driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
time.sleep(5)
for checkbox in checkboxes:
        if checkbox.get_attribute("value") == "option2":
            checkbox.click()
            break

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        assert checkbox.is_selected(), "checkbox is not selected"
        print ("checkbox is selected")
        break

radiobuttons = driver.find_elements(By.ID, "radio-btn-example")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected(), "radio button is not selected"
        print ("radio button is selected")
        break
