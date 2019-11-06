from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.poll-maker.com/results2580426xf8aC4A8e-74#tab-2")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Results Breakdown - Part 2 / 6'])[1]/following::div[4]").click()
        driver.find_element_by_id("qpN-3").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='With Google'])[1]/following::div[5]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


driver = webdriver.Chrome(executable_path='C:/Users/Damian/Desktop/chromedriver.exe')
driver.get("https://www.proxysite.com/")
driver.find_element_by_name("d").click()
driver.find_element_by_name("d").clear()
driver.find_element_by_name("d").send_keys("https://www.poll-maker.com/poll2580426xf8aC4A8e-74")
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Google'])[1]/following::button[1]").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Jared Ducharme, Sr., BMR-Hopedale'])[1]/input[1]").click()
driver.find_element_by_name("qp_b2580426").click()
driver.close()