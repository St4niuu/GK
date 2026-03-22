import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

choice = 0

center = (300, 300)
radius = 150
sides = 11

points = []

for i in range(sides):
    angle = 2 * math.pi * i / sides
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    points.append((x, y))

run = True
while run:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                choice = 0
            elif event.key == pygame.K_1:
                choice = 1
            elif event.key == pygame.K_2:
                choice = 2
            elif event.key == pygame.K_3:
                choice = 3
            elif event.key == pygame.K_4:
                choice = 4
            elif event.key == pygame.K_5:
                choice = 5
            elif event.key == pygame.K_6:
                choice = 6
            elif event.key == pygame.K_7:
                choice = 7
            elif event.key == pygame.K_8:
                choice = 8
            elif event.key == pygame.K_9:
                choice = 9
            else:
                run = False

    match choice:
        case 0:
            pygame.draw.polygon(win, CZERWONY , [(center[0] + (x - center[0]) * 1, center[1] + (y - center[1]) * 1) for x, y in points])
        case 1:
            pygame.draw.polygon(win, CZERWONY , [(center[0] + (x - center[0]) * 1.5, center[1] + (y - center[1]) * 1.5) for x, y in points])
        case 2:
            pygame.draw.polygon(win, CZERWONY , [
                (
                    center[0] + (x - center[0]) * math.cos(math.radians(45)) - (y - center[1]) * math.sin(math.radians(45)),
                    center[1] + (x - center[0]) * math.sin(math.radians(45)) + (y - center[1]) * math.cos(math.radians(45))
                )
                for x, y in points
            ])
        case 3:
            pygame.draw.polygon(win, CZERWONY , [(2 * center[0] - x, y) for x, y in points])
        case 4:
            pygame.draw.polygon(win, CZERWONY , [(x + 0.1 * y, y + 0.2 * x) for x, y in points])
        case 5:
            pygame.draw.polygon(win, CZERWONY , [(x, y - 50) for x, y in points])
        case 6:
            pygame.draw.polygon(win, CZERWONY , [(x + 0.5 * y, y + 0.1 * x) for x, y in points])
        case 7:
            pygame.draw.polygon(win, CZERWONY , [(x + 0.1 * y, y + 0.2 * x) for x, y in points])
        case 8:
            pygame.draw.polygon(win, CZERWONY , [
                (
                    center[0] + (x - center[0]) * math.cos(math.radians(275)) - (y - center[1]) * math.sin(math.radians(275)),
                    center[1] + (x - center[0]) * math.sin(math.radians(275)) + (y - center[1]) * math.cos(math.radians(275))
                )
                for x, y in points
            ])
        case 9:
            pygame.draw.polygon(win, NIEBIESKI , [(250, 150), (175, 75), (325, 75)])
            pygame.draw.rect(win, NIEBIESKI , (150, 150, 200, 100))
            pygame.draw.polygon(win, NIEBIESKI , [(250, 250), (175, 325), (325, 325)])

    pygame.display.update()
