#zad2
from array import *
tablica = array('u')
n = int(input("Ile znaków chcesz dodać do tablicy? "))
for i in range(n):
    tablica.append(input("Wprowadź znak "))
print("-------------------------")
print("Tablica przed odwróceniem")
print(tablica)
tablica.reverse()
print("-------------------------")
print("Tablica po odwróceniu")
print(tablica)

#zad3
import random
from array import *
tablica = array('d')
for i in range(10):
    tablica.append(random.uniform(-5, 5))
file = open("result.txt", "w")
file.write(str(tablica))
file.close()

#zad4
import numpy as np
a = np.array([[2,3,4,5,6],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]
             ], dtype=np.float64)
#Wyświetla w typie 64 bitowym, ponieważ inaczej jest overflow
for i in range(1,5):
    for j in range(5):
        a[i][j]=a[i-1][j]*a[i-1][j]

print(a)

#zad5
doc = input("Wpisz nazwe pliku:")
file = open(doc + ".txt")
histogram = {}
while True:
    char = file.read(1)
    if not char:
        break
    if (char in histogram):
        il = histogram.get(char)
        histogram[char] = il + 1
    else:
        histogram[char] = 1
file.close()
print(histogram)


#zad6
import random

def deck():
    deck = [('2', 'c'), ('2', 'd'), ('2', 'h'), ('2', 's'),
            ('3', 'c'), ('3', 'd'), ('3', 'h'), ('3', 's'),
            ('4', 'c'), ('4', 'd'), ('4', 'h'), ('4', 's'),
            ('5', 'c'), ('5', 'd'), ('5', 'h'), ('5', 's'),
            ('6', 'c'), ('6', 'd'), ('6', 'h'), ('6', 's'),
            ('7', 'c'), ('7', 'd'), ('7', 'h'), ('7', 's'),
            ('8', 'c'), ('8', 'd'), ('8', 'h'), ('8', 's'),
            ('9', 'c'), ('9', 'd'), ('9', 'h'), ('9', 's'),
            ('10', 'c'), ('10', 'd'), ('10', 'h'), ('10', 's'),
            ('J', 'c'), ('J', 'd'), ('J', 'h'), ('J', 's'),
            ('D', 'c'), ('D', 'd'), ('D', 'h'), ('D', 's'),
            ('K', 'c'), ('K', 'd'), ('K', 'h'), ('K', 's'),
            ('A', 'c'), ('A', 'd'), ('A', 'h'), ('A', 's')]
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return tuple(deck)


def deal(deck, n):
    list = []
    shuffled_deck = shuffle_deck(deck)
    x = 0
    for i in range(n):
        for j in range(5):
            list.append(shuffled_deck[x])
            x = x + 1

    print(list)


deal(deck(),5)
