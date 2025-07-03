import pygame as pyg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

def main():
    pyg.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return
        screen.fill("black")
        pyg.display.flip()

if __name__ == "__main__":
    main()
