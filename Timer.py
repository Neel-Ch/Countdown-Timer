import os
import time

class Timer:
    def __init__(self, countdown_time):
        self.time = countdown_time

    def start(self):
        numbers = {
        0 : ''' __
|  |
|__|''',
        1 : '''
  | 
  |''',
        2 : ''' __
 __|
|__''',
        3 : ''' __
 __|
 __|''',
        4 : '''
|__|
   |''',
        5 : ''' __
|__
 __|''',
        6 : ''' __
|__
|__|''',
        7 : ''' __
   |
   |''',
        8 : ''' __
|__|
|__|''',
        9 : ''' __
|__|
 __|'''
        }
        for i in range(self.time, -1, -1):
            for digit in list(str(i)):
                print(numbers[int(digit)])
            time.sleep(1)
            os.system('cls')

def __main__():
    timer = Timer(100)
    timer.start()

__main__()
