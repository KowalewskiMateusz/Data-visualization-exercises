from random import randint
import matplotlib.pyplot as plt
import numpy as np
import pygal

class Die():
    def __init__(self, number_of_sides=6):
        self.num_sides = number_of_sides

    def roll(self):
        return randint(1, self.num_sides)


die = Die()
die_2 = Die(10)
a = [0 for x in range(die.num_sides+die_2.num_sides)]
for i in range(40000):
    k = die.roll() + die_2.roll()
    a[k-1] = a[k-1] + 1


del a[0]
print(a)
max_result = die.num_sides+die_2.num_sides

hist = pygal.Bar()
hist.title = "ROLL DIE"
k=[]
for i in range(2,die.num_sides + die_2.num_sides+1):
    k.append(str(i))
hist.x_labels = k
hist.x_title = "Side"
hist.y_title = "Frequency of result"
hist.add('D6 + D10',a)
hist.render_to_file('die_roll.svg')