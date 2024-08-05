import random
import time
import os
import platform

def cls():
    SO = platform.system()
    if SO == "Windows":
        os.system("cls")
    else:
        os.system("clear")
