from pprint import pprint

import pygame as pg
from random import choice


class XmasTree:
    def __init__(self):
        self.areas = []
        self.toys_coords = []

    def draw_tree(self, surface):
        top = 400, 200
        for i in range(4):
            area = ((300 - 50 * i, 200 + top[1] * (i / 1.5)), (400, 100 + 100 * (i * 0.9)),
                    (500 + 50 * i, 200 + top[1] * (i / 1.5)))
            self.areas.append(area)
            pg.draw.polygon(surface, '#007700', area)

        pg.draw.rect(surface, 'brown', ((370, 600), (50, 100)))
        pg.draw.polygon(surface, 'yellow', ([400, 20], [440, 130], [340, 60], [460, 60], [360, 130]))
        # pprint(self.areas)

    def draw_toys(self, surface):
        self.toys_coords = []
        with open('points.txt', 'r') as f:
            for i in f.readlines():
                self.toys_coords.append(tuple(map(int, i.split(', '))))
        for i in self.toys_coords:
            pg.draw.circle(surface, 'white', i, 7)

    def choice_mode(self):
        global mode
        mode = int(input('Выберете режим работы (от 1 до (?)): '))

    def change_colors(self):
        global mode, tick
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

        if mode == 1:
            for i in self.toys_coords:
                pg.draw.circle(screen, choice(colors), i, 7)

        elif mode == 2:
            color = choice(colors)
            for i in self.toys_coords:
                if tick == 1:
                    pg.draw.circle(screen, color, i, 7)

        elif mode == 3:
            n = 0
            color = choice(colors)
            while n < 80:
                for i in self.toys_coords:
                    if tick % 5 == 0:
                        for j in range(n):
                            pg.draw.circle(screen, color, i, 7)
                    n = n % 80 + 1

    # def points.txt(self, pos):
    #     with open('points.txt.txt', 'a+') as f:
    #         f.write(str(pos) + '\n')
    #         pg.draw.circle(screen, 'red', pos, 7)


if __name__ == '__main__':
    tree = XmasTree()
    mode = None
    tree.choice_mode()

    pg.init()
    size = 800, 800
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    screen.fill('white')

    tree.draw_tree(screen)
    tree.draw_toys(screen)

    tick = 1
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # if event.type == pg.MOUSEMOTION:
            #     print(event.pos)
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     tree.points.txt(event.pos)
        tree.change_colors()
        tick = tick % 10 + 1
        print(tick)
        pg.display.flip()
        clock.tick(5)
