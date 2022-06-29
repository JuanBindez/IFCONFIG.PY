'''
Author: www.github.com/JuanBindez
Description: loops linux's ifconfig command for easy viewing
Python Version: 3.10
year: 2022
Local: Brazil
'''

import os
import time


def show_network():
    while 1 < 2:
        os.system("ifconfig")
        time.sleep(1)
        os.system("clear")

try:
    show_network()

except KeyboardInterrupt:
    print("você encerrou o programa")
