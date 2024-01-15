import bluetooth
import pygame

pygame.init()
pygame.display.set_mode((1,1))
clock = pygame.time.Clock()

# Connect to HC-05 device
bd_addr = "98:D3:11:FC:CA:02"

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, 1))

up = False
down = False
left = False
right = False
change = False

while 1:
    change = False

    # Get keyboard input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = True
                change = True
            elif event.key == pygame.K_DOWN:
                down = True
                change = True
            elif event.key == pygame.K_LEFT:
                left = True
                change = True
            elif event.key == pygame.K_RIGHT:
                right = True
                change = True
            elif event.key == pygame.K_ESCAPE:
                sock.close()
                break
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
                change = True
            elif event.key == pygame.K_DOWN:
                down = False
                change = True
            elif event.key == pygame.K_LEFT:
                left = False
                change = True
            elif event.key == pygame.K_RIGHT:
                right = False
                change = True
    
    # Send data to Arduino
    data = 64
    if up:
        data += 1
    if down:
        data += 2
    if left:
        data += 4
    if right:
        data += 8
    
    if change:
        print(data)
        sock.send(chr(data))
    
    clock.tick(60)