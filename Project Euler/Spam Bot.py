import pyautogui, time
time.sleep(5)

with open('names.txt') as f:
    a = f.read()

a = a.replace('"', '')
a = a.split(',')
a.sort()

string_1 = "I Love you <3 "

for num in range(1000000):
    pyautogui.typewrite(string_1)
    pyautogui.press("enter")

