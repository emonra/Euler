#rename to three digits
#eg. "123.py" will be renamed to "Problem 123.py"
import os

for index in range(1000):
	OldName = os.path.join(os.getcwd(), str(index) + ".py")
	if os.path.exists(OldName):
		if index < 10:
			NewName = os.path.join(os.getcwd(), "Problem " + "00" + str(index) + ".py")
		elif index < 100:
			NewName = os.path.join(os.getcwd(), "Problem " + "0" + str(index) + ".py")
		else:
			NewName = os.path.join(os.getcwd(), "Problem " + str(index) + ".py")
		os.rename(OldName, NewName)
exit(0)