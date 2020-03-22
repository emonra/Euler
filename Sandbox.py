#rename to three digits
import os
import time
while True:
	for index in range(1000):
		if index < 10:
			OldName = os.path.join(os.getcwd(), "00" + str(index) +".py")
		elif index <100:
			OldName = os.path.join(os.getcwd(), "0" + str(index) + ".py")
		else:
			OldName = os.path.join(os.getcwd(), str(index) + ".py")
		if os.path.exists(OldName):
			if index < 10:
				NewName = os.path.join(os.getcwd(), "Problem " + "00" + str(index) + ".py")
			elif index < 100:
				NewName = os.path.join(os.getcwd(), "Problem " + "0" + str(index) + ".py")
			else:
				NewName = os.path.join(os.getcwd(), "Problem " + str(index) + ".py")
			os.rename(OldName, NewName)
	time.sleep(5)