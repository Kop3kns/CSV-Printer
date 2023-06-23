from pynput.keyboard import Controller, Key
import time
import csv

time.sleep(5)

with open('merge-csv.com__64908c516cccd.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for id in row:
            keyboard = Controller()
            
            # Presses each character of the string 'id'
            for char in id:
                keyboard.press(char)
            keyboard.press(Key.enter)
            time.sleep(.025)