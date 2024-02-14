# # import pyautogui
# # import time
# # import cv2
# # import glob
# # x =1
# # screenshortnum = x*30
# # for i in range(screenshortnum):
# #     screenshot = pyautogui.screenshot()
# #     screenshot.save(f'./vraj/screenshot{i}.png')

# # frameSize = (500, 500)

# # out = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

# # for filename in glob.glob('./vraj/*.jpg'):
# #     img = cv2.imread(filename)
# #     out.write(img)

# # out.release()

# import cv2
# import numpy as np
# import glob

# frameSize = (500, 500)

# out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

# for filename in glob.glob('D:/images/*.jpg'):
#     img = cv2.imread(filename)
#     out.write(img)

# out.release()


# importing the required packages
import pyautogui
import cv2
import numpy as np

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording.avi"

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 60.0


# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 720, 1280)

while True:
	# Take screenshot using PyAutoGUI
	img = pyautogui.screenshot()

	# Convert the screenshot to a numpy array
	frame = np.array(img)

	# Convert it from BGR(Blue, Green, Red) to
	# RGB(Red, Green, Blue)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	out.write(frame)
	
	# Optional: Display the recording screen
	cv2.imshow('Live', frame)
	
	# Stop recording when we press 'q'
	if cv2.waitKey(1) == ord('q'):
		break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
