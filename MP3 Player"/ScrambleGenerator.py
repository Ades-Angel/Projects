import random

moves = ["U", "D", "F", "B", "R", "L"]
dir = ["", "'", "2"]
slen = random.randint(25, 28)


def scramble_gen():
    scramble = [0] * slen
    for x in range(len(scramble)):
        scramble[x] = [0] * 2
    return scramble


print(scramble_gen)
