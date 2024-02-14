import pyautogui
import time
# pyautogui.moveTo(50,40,duration=0)
# pyautogui.moveRel(20,80,duration=2)

# pyautogui.click(10,0,clicks=3,interval=0,button='left')

# pyautogui.typewrite("i am learning")

# pyautogui.press('enter')  # Presses a single key
# pyautogui.hotkey('ctrl', 'a')  # Presses a combination of keys

# screenshot = pyautogui.screenshot()
# screenshot.save('screenshot.png')
# screenshot.show()

# # Get the current mouse position
# original_x, original_y = pyautogui.position()

# # Move the mouse to a specific location
# target_x, target_y = 500, 500
# pyautogui.moveTo(target_x, target_y)
# # Sleep for a certain period (e.g., 5 seconds)
# time.sleep(5)

# # Move the mouse back to its original position
# pyautogui.moveTo(original_x, original_y)

import cv2
import numpy as np
img = cv2.imread('screenshot.png')
# cv2.imshow('Image',img)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()

# Create a black image (all zeros) of size 512x512
img = np.zeros((512, 512, 3), np.uint8)

# Draw a line from point (0,0) to (511,511) with color (blue in BGR format) and thickness 5
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Display the image
cv2.imshow('Line', img)
cv2.waitKey(0)
cv2.destroyAllWindows()bol