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
