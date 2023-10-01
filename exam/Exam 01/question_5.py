import pyautogui
import time

row = int(input())
time.sleep(5)

for i in range(1, row + 1):
    pyautogui.typewrite('#' * (i), interval=0.10)
    pyautogui.press("Enter") 
#
##
###
####
#####
######
#
##
###
####
#####
