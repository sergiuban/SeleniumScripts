import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\banse\\Downloads\\chromedriver_win32\\chromedriver.exe")

class TestingLogin():

    def LoginNotOk(self):


        driver.get("http://www.demo.guru99.com/V4/")


        user = driver.find_element_by_name("uid")
        user.send_keys("mngr335610")
        # user = "mngr335610"

        password = driver.find_element_by_name("password")
        password.send_keys("jAvEdUm_wrong")
        # password = "jAvEdUm"

        buttonLogin = driver.find_element_by_name("btnLogin")
        buttonLogin.click()

        time.sleep(10)

        try:
            actualTitle = driver.title
            print(actualTitle)
            if actualTitle == "Guru99 Bank Manager HomePage":
                print("TestCase Login Failed")

        except:
            print("TestCase Login NotOk Pass")

    def LoginOk(self):


        driver.get("http://www.demo.guru99.com/V4/")

        user = driver.find_element_by_name("uid")
        user.send_keys("mngr335610 ")
        #xpath_input[@title='Căutați']

        password = driver.find_element_by_name("password")
        password.send_keys("jAvEdUm")

        buttonLogin = driver.find_element_by_name("btnLogin")
        buttonLogin.click()

        try:
            actualTitle = driver.title
            print(actualTitle)
            if actualTitle == "Guru99 Bank Manager HomePage":
                print("TestCase Login Pass")

        except:
            print("TestCase Login Failed")


test = TestingLogin()
test.LoginOk()
test.LoginNotOk()

driver.quit()
