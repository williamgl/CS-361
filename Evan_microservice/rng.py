# Author: Evan Butler
# Reference:  https://github.com/evanbutler96/RNG/blob/main/rng.py

# Modified by: Gan Li

import random
import time

if __name__ == '__main__':

    print("Random Number Generator running\n")

    while True:
        time.sleep(1)
        with open('prng-service.txt', 'r') as f:
            read_data = f.readline()
            books = int(f.readline())

        if read_data == "run\n":
            index = random.randint(1, books)
            with open('prng-service.txt', 'w') as f:
                f.write(f'index\n{index}')
            print(f"Generated a new book index {index}\n")
