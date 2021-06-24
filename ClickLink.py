import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\banse\\Downloads\\chromedriver_win32\\chromedriver.exe")

class TestingClickLink():

    def clickLink(self):

        driver.get("http://demo.guru99.com/test/link.html")

        links = driver.find_elements_by_link_text("click here")
        for onelink in links:
            att = onelink.get_attribute('href')
            if att == "http://www.fb.com/":
                onelink.click()
                title = driver.title
                if "Facebook" in title:
                    print("Found")
                break

test = TestingClickLink()
test.clickLink()

driver.quit()
