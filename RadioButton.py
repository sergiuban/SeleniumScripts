import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\banse\\Downloads\\chromedriver_win32\\chromedriver.exe")

class TestingRadioButton():

    def radiobutton(self):

        driver.get("http://demo.guru99.com/test/radio.html")

        radio = driver.find_elements_by_xpath("//input[@type='radio']")

        # Variata pentru mai multe butoane
        # for x in radio:
        #     if x.is_selected():
        #         print("Button is selected")
        #     else:
        #         x.click()
        #         print("Button just selected")
        #         time.sleep(5)

        radio[0].click()
        time.sleep(5)
        if radio[0].is_selected():
            print("Button 1 is selected")

        radio[1].click()
        time.sleep(5)
        if radio[1].is_selected():
            print("Button 2 is selected")

        radio[2].click()
        time.sleep(5)
        if radio[2].is_selected():
            print("Button 3 is selected")

        #Var. 2 dupa id
        # driver.find_element_by_id("vfb-7-1").click()
        # driver.find_element_by_id("vfb-7-2").click()
        # driver.find_element_by_id("vfb-7-3").click()





radio = TestingRadioButton()
radio.radiobutton()

driver.quit()

# //input[@type='radio']
