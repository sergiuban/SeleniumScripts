import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\banse\\Downloads\\chromedriver_win32\\chromedriver.exe")

class DragAndDrop():

    def TestingDragAndDrop(self):

        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()

        pathIframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(pathIframe)

        fromElement = driver.find_element_by_id("draggable")
        toElement = driver.find_element_by_id("droppable")

        action = ActionChains(driver)
        action.drag_and_drop(fromElement, toElement)
        action.perform()

        time.sleep(10)



draganddrop = DragAndDrop()
draganddrop.TestingDragAndDrop()

driver.quit()




# //iframe[@class='demo-frame']

# //div[@id='draggable']
# //div[@id='droppable']
