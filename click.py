#!/usr/bin/python3
import pyautogui
import time
print("请在3秒内选择点击位置...")

for i in range(1,4):
	time.sleep(1)
	print(i)

a,b = pyautogui.position()

print(a,b)

for i in range(1,200):
	pyautogui.click(a,b,button='left')
	time.sleep(2)
	print(i)




