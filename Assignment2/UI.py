# Name: Gan Li
# Course: CS 361
# Assignment: 2
# Description: text based user interface.

import time
from PIL import Image

if __name__ == '__main__':
    while True:
        # request for input
        userInput = ''
        while userInput != '1' and userInput != '2':
            userInput = input('Please type in 1 to view a Genshin Impact picture, or 2 to exit:')
            if userInput != '1' and userInput != '2':
                print('Invalid input, please try again!')

        if userInput == '1':
            # write 'run' in prng-service.txt
            file = open('prng-service.txt', 'w')
            file.write('run')
            file.close()
            # sleep 5 seconds
            time.sleep(5)
            # read the prng generated random number from prng-service.txt
            file = open('prng-service.txt', 'r')
            line = file.readline()
            file.close()
            # write the random number in image-service.txt
            file = open('image-service.txt', 'w')
            file.write(line)
            file.close()
            # sleep 5 seconds
            time.sleep(5)
            # read the path from image-service.txt and display the image
            file = open('image-service.txt', 'r')
            path = file.readline()
            file.close()
            # it also prints the path in the terminal
            print('The path of the displayed picture is', path)
            pic = Image.open(path)
            pic.show()
        else:
            # input is 2 to exit
            exit()
