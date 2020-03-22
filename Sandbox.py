#rename to three digits
import os
for index in range(100):
	if index < 10:
		OldName = os.path.join(os.getcwd(), "Problem " + "0" + str(index) + ".py")
	else:
		OldName = os.path.join(os.getcwd(), "Problem " + str(index) + ".py")
	print(OldName)
	if os.path.exists(OldName):
		if index < 10:
			NewName = os.path.join(os.getcwd(), "Problem " + "00" + str(index) + ".py")
		else:
			NewName = os.path.join(os.getcwd(), "Problem " + "0" + str(index) + ".py")
		os.rename(OldName, NewName)
print("done")