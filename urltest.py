from selenium import webdriver
import time
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import randint
import webbrowser
import random
from selenium.webdriver.chrome.options import Options

class VideoGroup:
	def __init__(self,stringstuff):
		self.newssplits =  stringstuff.split(",")
		self.length = len(self.newssplits)
	def getLength():
		return self.length

#sets up the extentisions and tells the computer where the selenium driver is
def startProgram ():
	chrome_options = Options()
	#chrome_options.add_argument("--mute-audio") add in to mute audio
	chrome_options.add_argument("--mute-audio")
	chrome_options.add_extension('C:\\Users\\Matthew\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\ejddjiiombhjiejeclpkoebbepphohen\\1.6.7_0.crx')
	driver = webdriver.Chrome("C:\\Users\\Matthew\\Downloads\\chromedriver_win32\\chromedriver.exe",chrome_options=chrome_options)
	#captchaImg
	driver.get("http://www.swagbucks.com/p/login")
	before_rest = randint(2,5)
	time.sleep(before_rest)
	username = driver.find_element_by_id("sbxJxRegEmail")
	password = driver.find_element_by_id("sbxJxRegPswd")
	username.send_keys("mquan")
	middle_rest = randint(2,5)
	time.sleep(middle_rest)
	password.send_keys("derpderp")
	after_rest = randint(2,5)
	time.sleep(after_rest)
	password.send_keys(Keys.RETURN)
	time.sleep(3)
	listOfVideos = []
	#sbPlaylistVideos //this is the id for all of the sb videos

	#with open("choose_videos.txt") as f:
	with open("vid_list_final.txt") as f:
	    textfile = f.readlines()
	f.close()

	for i in textfile:
		test = VideoGroup(i)
		listOfVideos.append(test)


	for s in listOfVideos:
		driver.get(s.newssplits[0])
		bottom = driver.find_element_by_id('sbFooterWrap')
		hover = ActionChains(driver).move_to_element(bottom)
		hover.perform()
		time.sleep(2)
		bottom = driver.find_element_by_id('sbFooterWrap')
		hover = ActionChains(driver).move_to_element(bottom)
		hover.perform()
		time.sleep(2)
		content = driver.find_elements_by_class_name('sbTrayListItemHeaderImgContainerWrapper')
		driver.execute_script("return arguments[0].scrollIntoView();", content[int(s.newssplits[2])])
		hover = ActionChains(driver).move_to_element(content[int(s.newssplits[2])])
		hover.perform()
		after_rest = randint(2,5)
		time.sleep(after_rest)
		hover = ActionChains(driver).click(content[int(s.newssplits[2])])
		hover.perform()

		
		count = driver.find_elements_by_class_name('sbPlaylistVideo')
		print s.newssplits[0]
		print s.newssplits[2]
		print len(count)
		
		for idx,x in enumerate(count):
			nextOne = count[idx].find_element_by_class_name('sbPlaylistVideoNumber')
			action = ActionChains(driver).move_to_element(nextOne)
			action.perform()
			
			driver.execute_script("arguments[0].click();",nextOne) 
			after_rest = randint(5,12)
			time.sleep(after_rest)
			driver.execute_script("window.stop();") 
			#break_time = randint(4,8)
			#time.sleep(break_time)

			isExist = x.find_element_by_class_name('sbPlaylistVideoNumber')
			
			while isExist.text.isdigit() == True:
				print isExist.text
				break_time = randint(5,15)
				time.sleep(break_time)

	print time.strftime("%I:%M:%S")
	driver.quit()

startProgram ()