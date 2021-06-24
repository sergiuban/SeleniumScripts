import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\banse\\Downloads\\chromedriver_win32\\chromedriver.exe")

class TestingCheckBox():

    def checkbox(self):

        driver.get("http://demo.guru99.com/test/radio.html")

        checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")

        checkbox[0].click()
        time.sleep(5)
        if checkbox[0].is_selected():
            print("Button 1 is selected")

        checkbox[1].click()
        time.sleep(5)
        if checkbox[1].is_selected():
            print("Button 2 is selected")

        checkbox[2].click()
        time.sleep(5)
        if checkbox[2].is_selected():
            print("Button 3 is selected")

checkbox = TestingCheckBox()
checkbox.checkbox()

driver.quit()
