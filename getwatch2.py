from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException  
import time
from random import randint
import webbrowser
import random

def isexist(driver,num):
	try:
		driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/ol/li[" + str(x) + "]/div/div[1]/h3/a")
	except NoSuchElementException:
		return False
	return True

driver = webdriver.Chrome("C:\\Selenium_w\\chromedriver.exe")
driver.get("http://www.swagbucks.com/?sfp=h&t=w&p=1&isHomeMain=true&q=Alaskan+Klee+Kai")
before_rest = randint(2,5)
time.sleep(before_rest)
driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/table/tbody/tr/td[1]/div[2]/div[2]/iframe"))
#web /html/body/div[4]/div[2]/div[1]/table/tbody/tr/td[1]/div[2]/div[2]/iframe
#/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/ol
#/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/ol/li
#/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/ol/li[4]/div/div[1]


#/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/ol/li[1]/div/div[1]/h3/a
frame = driver.find_element_by_xpath('//*[@id="web"]')
before_rest = randint(5,7)
time.sleep(before_rest)
mainContent = driver.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/ol/li")
#element = mainContent.find_elements_by_tag_name("li")
#correctLink = mainContent.find_elements_by_class_name("res")
#/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/ol/li[4]/div/div[1]
correctLink = []
#for x in mainContent:
#	inside = x.find_element_by_class_name("res")
#	print "inside array : " + str(len(inside))
#	if isexist(inside) == True :
#		correctLink.append(x)

print len(mainContent)
#print len(correctLink)
#MAKE SURE TO USE ISEXIST TO CHECK FOR ELEMENT
for x in range(1, len(mainContent)):
	if isexist(driver,x) == True:	
		selector = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/ol/li[" + str(x) + "]/div/div[1]/h3/a")
		action = ActionChains(driver).move_to_element(selector)
		action.perform()
		driver.execute_script("arguments[0].click();",selector)
		before_rest = randint(5,10)
		time.sleep(before_rest)
		driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') 



##captchaImg
#element = driver.find_element_by_tag_name("res")
#for x in element:
#	content = driver.find_element_by_tag_name("div")
#	moreStuff = driver.find_element_by_tag_name("h3")