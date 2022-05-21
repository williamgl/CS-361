# Author: Evan Butler
# Reference:  https://github.com/evanbutler96/RNG/blob/main/ui.py

# Modified by: Gan Li

import time

if __name__ == '__main__':
    while True:
        print("Would you like to generate a random number?")
        val = input("Push 'Enter' to generate a number\n")
        f = open("prng-service.txt", "w")
        f.write("run")
        f.close()
        time.sleep(3.0)
        f = open("prng-service.txt", "r")
        number = f.readline()
        f = open("prng-service.txt", "r+")
        f.truncate(0)
        f.close()
        f = open("image-service.txt", "w")
        print(f"Your Random number is {number}\n")
