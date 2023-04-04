import pygame, pymunk, sys
from pymunk import Vec2d
pygame.init()
#display
resolution = display_width, display_height = (500, 500)
displaysurf = pygame.display.set_mode(resolution)

run = True

def quit_game():
    pygame.quit()
    sys.exit()

def coordinates_conversion(y):
    return -y + 600

#player
def main():
    player_x = 10
    player_y = 10
    player_size = 50
    player_body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
    player_shape = pymunk.Poly(player_body, (0, 0))
    pymunk.Space.add(player_shape)
    while run:
        pygame.draw.rect(displaysurf, (255, 255, 155), pygame.rect(player_x, player_y, player_size, player_size))

main()
