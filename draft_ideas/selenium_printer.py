import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


# function click_print(url):
driver = webdriver.Firefox()
driver.get("https://downshiftology.com/wprm_print/32832")
# driver.find_element(By.ID, "wprm-print-button-print").click()
driver.execute_script("window.print()")

webElement = driver.findElement(By.xpath("")) 
webElement.sendKeys(Keys.ENTER)

# driver.switch_to.window(driver.window_handles[-1])
# actionButton = driver.execute_script(
# "return document.querySelector('print-preview-app').shadowRoot.querySelector('#sidebar').shadowRoot.querySelector('print-preview-button-strip').shadowRoot.querySelector('.action-button')")



# cancelButton.click()
# # switch back to main window
# driver.switch_to.window(driver.window_handles[0])

time.sleep(0.5)

driver.close()


# tehre does not appear to be a good way to interact with a system print dialog 