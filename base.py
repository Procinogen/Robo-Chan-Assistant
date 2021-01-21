#Non-AI related Modules
import time
import numpy
#AI-related Modules
import learn

#Actual Code
print ("Hello, world!")

#Command input
def Run():
	resp = input("How may I help you? ")
	
	return

#Waits for input
def waitForCommand():
	try:
		while True:
			time.sleep(1)  # 1s
	except KeyboardInterrupt:
		Run()
	return
	
waitForCommand()