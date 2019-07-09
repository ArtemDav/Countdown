from time import sleep
from colorama import Fore
from os import system


def main():
    time = 55
    while True:
        hour = time // 3600
        minutes = (time - hour * 3600) // 60
        seconds = time % 60
        print(Fore.GREEN + str(hour) + " h. " + str(minutes) + " m. " + str(seconds) + " s.")
        time += 1
        sleep(1)
        system("cls")


main()
