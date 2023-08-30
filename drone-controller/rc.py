import asyncio
from tello_asyncio import Tello
from sprite import *
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_w,
    K_s,
    K_a,
    K_d,
    K_SPACE,
    K_LSHIFT,
    KEYDOWN,
    QUIT,
)

async def main():
    my_drone = Tello()
    await my_drone.connect()
    print(await my_drone.query_battery())
    await my_drone.send(f"rc 0 0 0 0")
    await my_drone.takeoff()

    init()
    setScreen(500, 500)

    while run():
        setBackground((255, 255, 255))

        #from easytello docs -100-100
        a = 0 #left / right
        b = 0 #forward / backward
        c = 0 #up / down
        d = 0 #yaw (not implemented)

        keys = getKeys()
        print(keys)
        if keys[K_a]:
            a -= 1
        if keys[K_d]:
            a += 1
        if keys[K_w]:
            b += 1
        if keys[K_s]:
            b -= 1
        if keys[K_SPACE]:
            c += 1
        if keys[K_LSHIFT]:
            c -= 1
        if keys[K_LEFT]:
            d -= 1
        if keys[K_RIGHT]:
            d += 1
        multiplier = 50
        await my_drone.send(f"rc {a*multiplier} {b*multiplier} {c*multiplier} {d*multiplier}")

        pygame.display.flip()

    await my_drone.land()

asyncio.run(main())