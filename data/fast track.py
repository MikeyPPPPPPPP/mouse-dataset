
import pyautogui
import time



print("Ctrl c   to stop")
with open('data.txt',"w") as file:
	try:
		while True:
			time.sleep(.01)
			x, y = pyautogui.position()
			points = f"{x}, {y}"
			file.write(points+"|")
			file.flush()
	except KeyboardInterrupt:
		file.close()




		
