import matplotlib.pyplot as plt
from random import choice
import time


class random_walk():
    def __init__(self, number_of_points=5000):
        self.number_of_points = number_of_points
        self.x_values = [0]
        self.y_values = [0]

    def walk(self):
        while len(self.x_values) < self.number_of_points:
            x_direction = choice([-1, 1])
            y_direction = choice([-1, 1])
            x_step = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_walk = x_direction * x_step
            y_walk = y_direction * y_step

            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_walk
            next_y = self.y_values[-1] + y_walk

            self.x_values.append(next_x)
            self.y_values.append(next_y)


plt.ion()
fig = plt.figure()
while True:
    rw = random_walk(5000)
    rw.walk()
    point_numbers = list(range(rw.number_of_points))
    plt.scatter(rw.x_values, rw.y_values, s=1, edgecolors='none', c=point_numbers, cmap=plt.cm.prism)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.title("Random walk", fontsize=30)
    plt.xlabel("Os X", fontsize=20)
    plt.ylabel("Os Y", fontsize=20)
    plt.tick_params(axis="both", labelsize=12)
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(1)
    plt.cla()
