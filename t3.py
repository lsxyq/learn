import time
from selenium import webdriver
PATH= r"C:\Users\teacher\AppData\Local\Google\Chrome\Application\chrome.exe"
browser = webdriver.Chrome()
browser.set_window_size(1055, 800)
browser.get("http://www.yooli.com/")
browser.find_element_by_id("idClose").click()
time.sleep(5)

browser.save_screenshot("shot.png")
browser.quit()