# Name: Gan Li
# Course: CS 361
# Assignment: 2
# Description: Input: non-negative integer i. Output, the ith image in a set.

import time

if __name__ == '__main__':
    while True:
        # sleep for 1 second
        time.sleep(1)

        # open image-service.txt and read the command line
        file = open('image-service.txt', 'r')
        line = file.readline()
        file.close()

        # if line in file is a number:
        try:
            num = int(line)
        except ValueError:
            pass
        else:
            # generate the mod number so that we only have 1 to 6
            num %= 6
            num += 1
            # write the path to image-service.txt
            path = './img/' + str(num) + '.png'
            file = open('image-service.txt', 'w')
            file.write(path)
            file.close()
