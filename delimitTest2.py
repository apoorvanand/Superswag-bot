class VideoGroup:
	def __init__(self,stringstuff):
		self.newsplits =  stringstuff.split(",")
		self.length = len(self.newsplits)
	def getLength():
		return self.length
		
def startProgram () :
	with open("vid_list.txt") as f:
	    textfile = f.readlines()
	f.close()


	print "len text file: " + str(len(textfile))
	listOfVideos = []
	for i in textfile:
		test = VideoGroup(i)
		listOfVideos.append(test)

	for j in listOfVideos:
		print j.newsplits[0]
		print j.newsplits[1]


	print "**************************************"

	listOfVideos.sort(key=lambda x: int(x.newsplits[1]), reverse=False)

	print "len : " + str(len(listOfVideos)) 

	file = open('vid_list_final.txt','w')
	count1 = 0
	count2 = 0
	for j in listOfVideos:
		print j.newsplits[1]
		file.write(j.newsplits[0] + ",")
		file.write(j.newsplits[1] + ",")
		file.write(j.newsplits[2])
		

	file.close()

startProgram()