from selenium import webdriver




driver = webdriver.Chrome(executable_path='C:/Users/Damian/Desktop/chromedriver.exe')
driver.get("https://www.proxysite.com/")
driver.find_element_by_name("d").click()
driver.find_element_by_name("d").clear()
driver.find_element_by_name("d").send_keys("https://www.poll-maker.com/poll2580426xf8aC4A8e-74")
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Google'])[1]/following::button[1]").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Jared Ducharme, Sr., BMR-Hopedale'])[1]/input[1]").click()
driver.find_element_by_name("qp_b2580426").click()
driver.close()