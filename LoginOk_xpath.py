from selenium import webdriver

class TestingLogin():

    def LoginOk(self):

        driver = webdriver.Chrome(executable_path="C:\\Users\\banse\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://www.demo.guru99.com/V4/")

        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys("mngr335610 ")
        #xpath = //input[@name='uid']

        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys("jAvEdUm")
        #xpath = //input[@name='password']

        buttonLogin = driver.find_element_by_xpath("//input[@name='btnLogin']")
        buttonLogin.click()
        #xpath = //input[@name='btnLogin']

        try:
            actualTitle = driver.title
            print(actualTitle)
            if actualTitle == "Guru99 Bank Manager HomePage":
                print("TestCase Login Pass")

        except:
            print("TestCase Login Failed")


test = TestingLogin()
test.LoginOk()
