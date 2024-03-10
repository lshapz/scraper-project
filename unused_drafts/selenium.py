from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


# function click_print(url):
driver = webdriver.Firefox()
driver.get("https://downshiftology.com/wprm_print/32832")
# driver.find_element(By.ID, "wprm-print-button-print").click()
driver.execute_script("window.print()")
Alert(driver).accept()
driver.close()
