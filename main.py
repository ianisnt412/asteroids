import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SHOOT_CD
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0   
    

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (updatable_group, drawable_group, asteroid_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (updatable_group, drawable_group, shots_group)

    asteroid_field = AsteroidField() 
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable_group.update(dt)
        
        for asteroid in asteroid_group:
            if asteroid.collision(player) == True:
                print("==== You crashed!! ==== \n ==== GAME OVER ====")
                sys.exit()
        
        for asteroid in asteroid_group:
            for shot in shots_group:                
                if asteroid.collision(shot) == True:
                    asteroid.split()
                    shot.kill()
            
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        print(dt)

    

if __name__ == "__main__":
    main()
