# Python code for displaying the image of the circuit of ICs connected on breadboard

import pygame

# Initialize pygame
NumConnections = []
conndict = []


def getcolor(num):
    if num == 0:
        return (0, 0, 255)
    elif num == 1:
        return (255, 0, 0)


pygame.init()
f = open("testfile.txt", "r")
line = f.readline().strip()
res = [int(i) for i in line.split() if i.isdigit()]
numICs = res[0]
for i in range(int(numICs)):
    line = f.readline().strip()
    res = [int(i) for i in line.split() if i.isdigit()]
    numConnections = res[0]
    NumConnections.append(int(numConnections))
    for i in range(int(numConnections)):
        line = f.readline().strip()
        line = f.readline().strip()

k = 0
for i in NumConnections:
    k += 1
    for j in range(i):
        line = f.readline().strip()
        res = [int(i) for i in line.split() if i.isdigit()]
        dict = [k, res]
        conndict.append(dict)

# write code to product numbers in list
productConnections = 1
for i in range(int(numICs)):
    productConnections *= NumConnections[i]

WINDOW_SIZE = (800, 600)

# Set the colors
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

# Set the positions of the ICs and the pins
ic1_x = 100
ic1_y = 250
ic2_x = 500
ic2_y = 250

ic_spacing = 100
pin_spacing = 20

connections = []
if numICs != 1:
    for i in range(int(productConnections)):
        line = f.readline().strip()
        line = line.split(": ")
        if (line[1] == "Yes"):
            res = [int(i) for i in line[0].split() if i.isdigit()]
            connections.append((res[0], res[1]))

# Set up the screen
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("IC Connections")

# Clear the screen
screen.fill(BACKGROUND_COLOR)
# Draw the ICs

for i in range(7):
    pygame.draw.rect(screen, LINE_COLOR, (ic1_x - 1, ic1_y - 70, 140, 140), 2)
    if numICs != 1:
        pygame.draw.rect(screen, LINE_COLOR,
                         (ic2_x - 1, ic2_y - 70, 140, 140), 2)
    font = pygame.font.SysFont(None, 24)
    number_surface = font.render(str(i+8), True, LINE_COLOR)
    screen.blit(number_surface, (ic1_x + pin_spacing * i, ic1_y - 60))
    number_surface = font.render(str(i+1), True, LINE_COLOR)
    screen.blit(number_surface, (ic1_x + pin_spacing * i, ic1_y + 50))
    if numICs != 1:
        number_surface = font.render(str(i+8), True, LINE_COLOR)
        screen.blit(number_surface, (ic2_x + pin_spacing * i, ic2_y - 60))
        number_surface = font.render(str(i+1), True, LINE_COLOR)
        screen.blit(number_surface, (ic2_x + pin_spacing * i, ic2_y + 50))
    for k in conndict:
        if k[0] == 1:
            if k[1][0] == i+8:
                pygame.draw.circle(screen, getcolor(k[1][1]),
                                   (ic1_x + pin_spacing * i + 5, ic1_y - 80), 5)
            elif k[1][0] == i+1:
                pygame.draw.circle(screen, getcolor(k[1][1]),
                                   (ic1_x + pin_spacing * i + 5, ic1_y + 80), 5)
        if numICs != 1:
            if k[0] == 2:
                if k[1][0] == i+8:
                    pygame.draw.circle(screen, getcolor(k[1][1]),
                                       (ic2_x + pin_spacing * i + 5, ic2_y - 80), 5)
                elif k[1][0] == i+1:
                    pygame.draw.circle(screen, getcolor(k[1][1]),
                                       (ic2_x + pin_spacing * i + 5, ic2_y + 80), 5)

# Draw the connections between the pins
j = 0
for conn in connections:
    number_surface = font.render(
        bytes(str(conn[0]), 'utf-8'), True, LINE_COLOR)
    screen.blit(number_surface, (ic1_x + pin_spacing * i - 10, ic1_y + 95 + j))
    pygame.draw.line(screen, LINE_COLOR, (ic1_x + pin_spacing * i,
                     ic1_y + 100 + j), (ic2_x + pin_spacing * 0, ic2_y + 100 + j), 3)
    number_surface = font.render(
        bytes(str(conn[1]), 'utf-8'), True, LINE_COLOR)
    screen.blit(number_surface, (ic2_x + pin_spacing * 0 + 4, ic2_y + 95 + j))
    j += 50

# Update the display
pygame.display.flip()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
