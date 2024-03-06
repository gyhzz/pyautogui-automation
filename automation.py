import pyautogui
import time

# # Wait
# time.sleep(3)

# # Get screen size
# print(pyautogui.size())

# # Get current mouse position
# print(pyautogui.position())

# # Move mouse to absolute position
# pyautogui.moveTo(3000, 100, 3)

# # Move mouse to relative position
# pyautogui.moveRel(100, 100, 3)

# Click on absolute position
# pyautogui.click(206, 164)

# Scroll up
# pyautogui.scroll(-900)

# coordinates = {'change ': ()}

# def click(position: tuple, seconds: int) -> None:

#     pass

time.sleep(3)
print(pyautogui.position())

'''
Positions
Outside Swap Box: (2118, 359)
Select Token: (2846, 321)
Unlock Token: (2687, 704)
Inside MM Box: (3142, 257)
Spending Cap: (3260, 405)
MM Next/Approve: (3353, 559)
'''

def perform_unlock_task():

    pyautogui.click(2118, 359)
    pyautogui.scroll(1000)
    pyautogui.click(2687, 704)
    time.sleep(7)
    pyautogui.click(3142, 257)
    pyautogui.scroll(1000)
    pyautogui.doubleClick(3260, 405)
    pyautogui.press('1')
    pyautogui.scroll(-1000)
    time.sleep(3)
    pyautogui.click(3353, 559)
    time.sleep(3)
    pyautogui.click(3353, 559)
    time.sleep(20)


# Change Token Task
    
    