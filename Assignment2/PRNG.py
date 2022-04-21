# Name: Gan Li
# Course: CS 361
# Assignment: 2
# Description: Generates pseudo-random numbers (PRNG services)

import random
import time

if __name__ == '__main__':
    while True:
        # sleep for 1 second
        time.sleep(1)

        # open prng-service.txt and read the command line
        file = open('prng-service.txt', 'r')
        line = file.readline()
        file.close()

        # if line in file is run:
        if line == 'run':
            # print the 'run' in terminal to show UI changed prng-service.txt
            print(line)
            # write a random number between 1 and 300 in prng-service.txt
            file = open('prng-service.txt', 'w')
            file.write(str(random.randint(1, 300)))
            file.close()
