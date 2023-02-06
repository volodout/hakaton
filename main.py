import pygame as pg
from random import choice, sample

COLORS = ['red', 'orange', 'yellow', 'Cyan', 'blue', 'purple', 'Magenta', 'Lime']


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
        pg.draw.polygon(surface, 'red', ([400, 20], [440, 130], [340, 60], [460, 60], [360, 130]))
        pg.draw.polygon(surface, 'red', ([386, 60], [414, 60], [424, 87], [400, 103], [375, 87]))
        # pprint(self.areas)

    def draw_toys(self, surface):
        self.toys_coords = []
        with open('points.txt', 'r') as f:
            for i in f.readlines():
                self.toys_coords.append(tuple(map(int, i.split())))
        for i in self.toys_coords:
            pg.draw.circle(surface, 'white', i, 7)

    def choice_mode(self):
        global garland_mode
        output = ['Мерцание разными цветами', 'Мерцание одним цветом', 'Мерцание двумя цветами', 'Мерцание "змейкой"']
        print('Доступные режимы гирлянды: 1 2 3 4')
        try:
            garland_mode = int(input('Выберите режим (укажите цифру): '))
            if garland_mode not in range(1, 5):
                raise Exception
            print('-----------------------------------------------')
            print(f'Выбранный режим [{garland_mode}] : {output[garland_mode - 1]}')
            print('-----------------------------------------------')
        except Exception:
            print('-----------------------------------------------')
            print('Ошибка: выберите режим из списка')
            print('-----------------------------------------------')
            self.choice_mode()

    def change_colors(self, mode, ticks):
        if mode == 1:
            for i in self.toys_coords:
                if ticks % 2 == 0:
                    pg.draw.circle(screen, choice(COLORS), i, 7)

        elif mode == 2:
            color = choice(COLORS)
            for i in self.toys_coords:
                if ticks % 5 == 0:
                    pg.draw.circle(screen, color, i, 7)

        elif mode == 3:
            global c1, c2, n3
            if ticks % 12 == 0:
                for i in range(0, len(self.toys_coords), 2):
                    pg.draw.circle(screen, c1, self.toys_coords[i], 7)
                for i in range(1, len(self.toys_coords), 2):
                    pg.draw.circle(screen, c2, self.toys_coords[i], 7)
                c1, c2 = c2, c1
                n3 += 1
            if n3 == 4:
                c1, c2 = sample(COLORS, k=2)
                n3 = 0

        elif mode == 4:
            global color3, num
            for i in range(num):
                pg.draw.circle(screen, color3, self.toys_coords[i], 7)
            pg.draw.circle(screen, 'yellow', self.toys_coords[num - 1], 7, 1)
            num += 1
            if num > 125:
                pg.draw.circle(screen, color3, self.toys_coords[-1], 7)
                old_color = color3
                color3 = choice(COLORS)
                num = 1
                while color3 == old_color:
                    color3 = choice(COLORS)



    # def points(self, pos):
    #     with open('points.txt', 'a+') as f:
    #         f.write(str(pos[0]) + ' ' + str(pos[1]) + '\n')
    #         pg.draw.circle(screen, 'red', pos, 7)


if __name__ == '__main__':
    tree = XmasTree()
    garland_mode = None
    tree.choice_mode()
    if garland_mode == 3:
        c1, c2 = sample(COLORS, k=2)
        n3 = 0
    if garland_mode == 4:
        color3 = choice(COLORS)
        num = 1


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
            #     tree.points(event.pos)
        tree.change_colors(garland_mode, tick)
        tick = tick % 50 + 1
        # print(tick)
        pg.display.flip()
        clock.tick(15)
