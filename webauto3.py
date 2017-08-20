from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException  
import time
from random import randint
import webbrowser
import random



def isexist(element):
	try:
		element.find_element_by_class_name("playlistWasWatched")
	except NoSuchElementException:
		return False
	return True

#sbWatchCardItemsNum
def startProgram():

	driver = webdriver.Chrome("Insert the location of the webdriver")

	driver.get("http://www.swagbucks.com/p/login")

	time.sleep(15)

	file = open('vid_list.txt','w')
	#list of webpages may not be updated
	webpagelist = [
	"http://www.swagbucks.com/watch/playlists/111/editors-pick",
	"http://www.swagbucks.com/watch/playlists/133/entertainment",
	"http://www.swagbucks.com/watch/playlists/1/careers",
	"http://www.swagbucks.com/watch/playlists/98/fashion",
	"http://www.swagbucks.com/watch/playlists/101/fitness",
	"http://www.swagbucks.com/watch/playlists/4/health",
	"http://www.swagbucks.com/watch/playlists/650/hobbies",
	"http://www.swagbucks.com/watch/playlists/12/home-garden",
	"http://www.swagbucks.com/watch/playlists/447/music",
	"http://www.swagbucks.com/watch/playlists/333/news-politics",
	"http://www.swagbucks.com/watch/playlists/1999/personal-finance",
	"http://www.swagbucks.com/watch/playlists/91/pets-animals",
	"http://www.swagbucks.com/watch/playlists/692/shopping",
	"http://www.swagbucks.com/watch/playlists/129/travel",
	"http://www.swagbucks.com/watch/playlists/120/wedding",
	"http://www.swagbucks.com/watch/playlists/3/food",
	"http://www.swagbucks.com/watch/playlists/138/parenting",
	"http://www.swagbucks.com/watch/playlists/17/sports",
	"http://www.swagbucks.com/watch/playlists/22/technology"]

	for t in webpagelist:
		driver.get(t)
		bottom = driver.find_element_by_id('sbFooterWrap')
		hover = ActionChains(driver).move_to_element(bottom)
		hover.perform()
		time.sleep(3)
		
		content = driver.find_elements_by_class_name('sbTrayListItemHeaderImgContainerWrapper')
		title = driver.find_element_by_id('sbShopSortLabel')
		el3 = driver.find_elements_by_css_selector(".sbTrayListItemHeader.watchItemHeader")
		slotPos = 0

		for num in el3:
			if isexist(num) == False:
				numOfVideos = num.find_element_by_class_name('sbWatchCardItemsNum')
				file.write(''.join(t) + ",")
				file.write(numOfVideos.text + ",")
				print numOfVideos.text
				file.write(str(slotPos))
				
				file.write('\n')
			slotPos = slotPos + 1


	file.close()
	driver.quit()

startProgram()