import os
import time


def sensor():
    while 10 < 50:
        os.system("ifconfig")
        time.sleep(1)
        os.system("clear")

try:
    sensor()

except KeyboardInterrupt:
    print("você encerrou o programa")
