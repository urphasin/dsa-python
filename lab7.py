"""
Lab 7: Boggle Game

Pseudocode:

build the boggle core functions

run game loop.
"""


import random

def buildboggle() -> list[list]:
    grid = []
    hashtable = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z",
    }

    for row in range(5):
        col = []
        for j in range(5):
            rnd = random.randint(1, 26)
            entry = hashtable.get(rnd)
            col.append(entry)
        grid.append(col)

    return grid

def printboggle(grid: list[list]) -> None:
    print("5 x 5 Boggle:\n")
    for row in grid:
        for col in row:
            print(col, end=" ")
        print()



grid__Instance = buildboggle()
printboggle(grid__Instance)

letter_points = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1,
    "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
    "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
    "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
    "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4,
    "Z": 10
}

while True:
    print()
    q = input("Enter a word: (q to quit): ")
    if q == "q":
        print("Goodbye!")
        break
    score = 0
    for letter in q.upper():
        score += letter_points[letter]
    print("Score:", score)








