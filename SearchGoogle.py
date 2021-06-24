import time

from selenium import webdriver

class ChromeDriverWindows():

    def searchGoogle(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\banse\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.google.com/")

        element = driver.find_element_by_id("L2AGLb")
        element.click()

        element_search = driver.find_element_by_name("q")
        element_search.send_keys("selenium")
        element_search.submit()


        time.sleep(5)


search = ChromeDriverWindows()
search.searchGoogle()
