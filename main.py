from time import sleep
from colorama import Fore
from os import system


def main():
    time = 55
    while True:
        hour = time // 3600
        minutes = (time - hour * 3600) // 60
        seconds = time % 60
        print(Fore.GREEN + str(hour) + " ч. " + str(minutes) + " мин. " + str(seconds) + " сек.")
        time += 1
        sleep(1)
        system("cls")


main()
