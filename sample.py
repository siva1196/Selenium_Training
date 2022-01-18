import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window() 
element = driver.find_element_by_class_name('gLFyf.gsfi')
element.send_keys('Selenium')
time.sleep(5)
element.submit()
driver.close()