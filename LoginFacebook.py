import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\banse\\Downloads\\chromedriver_win32\\chromedriver.exe")

class Facebook():

    def login(self):
        driver.get("https://www.facebook.com/")

        acceptAll = driver.find_element_by_xpath("//button[contains(text(),'Acceptă tot')]")
        acceptAll.click()

        email_input = driver.find_element_by_xpath("//input[@id='email']")
        email_input.send_keys("email")

        pass_input = driver.find_element_by_xpath("//input[@id='pass']")
        pass_input.send_keys("password")

        buttonLogin = driver.find_element_by_xpath("//button[contains(text(),'Conectează-te')]")
        buttonLogin.click()

        time.sleep(15)

    #xpath = //button[contains(text(),'Acceptă tot')]
    #xpath = //input[@id='email']
    #xpath = //input[@id='pass']
    #xpath = //button[contains(text(),'Conectează-te')]



fb = Facebook()
fb.login()
driver.quit()
