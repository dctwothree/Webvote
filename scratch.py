from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


driver = webdriver.Chrome(executable_path='C:/Users/Damian/Desktop/chromedriver.exe')

driver.get("https://www.poll-maker.com/results2580426xf8aC4A8e-74#tab-2")

assHole = driver.find_element_by_id("qpN-3.ex-num")


print(assHole)


#driver.find_element_by_id("qpN-3").click()