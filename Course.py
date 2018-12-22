import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from http.client import HTTPException


class courseTitle:
    def __init__(self, dept, courseID, waitTime=360):
        self.dept = dept
        self.course = courseID
        self.wait = waitTime

    def checkCourseAvailability(self):
        raw_html = self._getRawHtml()
        html = BeautifulSoup(raw_html, 'html.parser')

        for tr in html.select('tr'):
            if tr.find(text=self.course) is not None:
                if tr.find(text='OPEN') is not None:
                    return True
        return False

    def pauseTime(self):
        time.sleep(self.wait)

    def _getRawHtml(self):
        try:
            driver = webdriver.Firefox()
            driver.get('https://www.reg.uci.edu/perl/WebSoc')

            select = Select(driver.find_element_by_name("Dept"))
            select.select_by_value(self.dept)

            enterElement = driver.find_element_by_name("Submit")
            enterElement.click()

            raw_html = driver.page_source

        except HTTPException:
            print('[-] Connection Error')
        finally:
            driver.close()
        return raw_html
