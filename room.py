from random import randint

import pygame as pg


def draw_room():
    room_surface = pg.display.set_mode((1200, 800))

    pg.draw.rect(room_surface, '#BC9665', ([0, 0], [1200, 630]))  # wall
    for i in range(12):
        pg.draw.rect(room_surface, '#CDA776', ([100 * i, 0], [50, 630]))

    pg.draw.rect(room_surface, '#006060', ([0, 630], [1200, 200]))  # floor
    for i in range(5):
        pg.draw.rect(room_surface, '#117171', ([0, 650 + 40 * i], [1200, 20]))

    pg.draw.rect(room_surface, 'MidnightBlue', ([450, 50], [300, 400]))  # stars
    for i in range(10):
        x, y = randint(470, 730), randint(70, 430)
        pg.draw.circle(room_surface, 'SteelBlue', (x, y), 3)

    pg.draw.rect(room_surface, '#DDD6BA', ([450, 50], [300, 400]), 20)  # window
    pg.draw.rect(room_surface, '#DDD6BA', ([590, 50], [20, 400]), 20)
    pg.draw.rect(room_surface, '#DDD6BA', ([450, 190], [290, 20]), 20)

    pg.draw.rect(room_surface, 'Salmon', ([670, 440], [450, 250]), 0, 20)  # sofa
    pg.draw.rect(room_surface, 'DarkRed', ([670, 570], [450, 40]))
    pg.draw.rect(room_surface, 'IndianRed', ([670, 600], [450, 90]))
    pg.draw.rect(room_surface, '#EE5C5C', ([630, 540], [70, 150]), 0, 10)
    pg.draw.rect(room_surface, '#EE5C5C', ([1090, 540], [70, 150]), 0, 10)

    pg.draw.rect(room_surface, 'Orange', ([180, 650], [70, 70]))
    pg.draw.rect(room_surface, '#EE8300', ([180, 650], [70, 5]))
    pg.draw.rect(room_surface, 'Orange', ([175, 635], [80, 15]))
    pg.draw.rect(room_surface, 'OrangeRed', ([205, 635], [20, 85]))

    pg.draw.rect(room_surface, 'khaki', ([355, 670], [80, 40]))
    pg.draw.rect(room_surface, '#BDB76B', ([355, 670], [80, 5]))
    pg.draw.rect(room_surface, 'Coral', ([350, 655], [90, 15]))
    pg.draw.rect(room_surface, '#4169E1', ([370, 655], [10, 55]))
    pg.draw.rect(room_surface, '#4169E1', ([355, 680], [80, 10]))
    return room_surface


if __name__ == '__main__':
    pg.init()
    size = 1200, 800
    screen = pg.display.set_mode(size)
    screen.blit(draw_room(), (0, 0))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            pg.display.flip()
