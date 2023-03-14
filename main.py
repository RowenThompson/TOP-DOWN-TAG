import pygame, sys

#display screen
resolution = displaysurf_width, displaysurf_height = (1920, 1080)
displaysurf = pygame.display.set_mode(resolution)
game_name = "Top Down Tag"
game_display_name = pygame.display.set_caption(game_name)
game_icon = pygame.image.load("TOP-DOWN-TAG\\graphics\\wall_tile.png")
game_display_icon = pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()

#game_state can = main_menu, options, and tag
game_state = 'tag'

#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


#collision
collision_tolerance = 10

#tiles and map
tile_size = 64
ground_tile = pygame.image.load("TOP-DOWN-TAG\\graphics\\ground_tile.png")
ground_tile = pygame.transform.scale(ground_tile, (tile_size, tile_size))

wall_tile = pygame.image.load("TOP-DOWN-TAG\\graphics\\wall_tile.png")
wall_tile = pygame.transform.scale(wall_tile, (tile_size, tile_size))

enemy_png = pygame.image.load("TOP-DOWN-TAG\\graphics\\enemy.png")
enemy_png = pygame.transform.scale(enemy_png, (tile_size, tile_size))

tile_rect_list = []
tile_collide_rect_list = []
enemy_rect_list = []

#level 1
map1 = """wwwwwwwwwwwwwwwwwwwwwwwwwwwwww
w                            w
w                            w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w                  w
w         w e                w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwww

"""

map1 = map1.splitlines()

def tiles(map1):
    global ground_tile
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c == "g":
                ground_rect = displaysurf.blit(ground_tile, (x * tile_size, y * tile_size))
            if c == "w":
                wall_rect = displaysurf.blit(wall_tile, (x * tile_size, y * tile_size))
                tile_rect_list.append(wall_rect)
                tile_collide_rect_list.append(wall_rect)
            if c == "e":
                enemy_rect = displaysurf.blit(enemy_png, (x * tile_size, y * tile_size))
                enemy_rect_list.append(enemy_rect)
def quit():
    pygame.quit()
    sys.exit()

def update_display():
    pygame.display.update()

def game_loop():
    #player
    player_color = blue
    player_speed = 6
    player_x = 500
    player_y = 500
    player_rect = pygame.draw.rect(displaysurf, player_color, pygame.Rect(player_x, player_y, tile_size, tile_size))
    while game_state == 'tag':
        displaysurf.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_w]:
            player_y -= player_speed
        if keys[pygame.K_s]:
            player_y += player_speed
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_d]:
            player_x += player_speed
        tiles(map1)
        #for tile_rect in tile_rect_list:
        collision_index = player_rect.collidelist(tile_rect_list)
        if player_rect.collidelist(tile_rect_list) > -1:
            if abs(player_rect.top - tile_rect_list[collision_index].bottom) < collision_tolerance:
                player_y += 7
            if abs(player_rect.bottom - tile_rect_list[collision_index].top) < collision_tolerance:
                player_y -= 7
            if abs(player_rect.right - tile_rect_list[collision_index].left) < collision_tolerance:
                player_x -= 7
            if abs(player_rect.left - tile_rect_list[collision_index].right) < collision_tolerance:
                player_x += 7
        player_rect = pygame.draw.rect(displaysurf, player_color, pygame.Rect(player_x, player_y, tile_size, tile_size))
        update_display()
        clock.tick(60)





if __name__ == '__main__':
    game_loop()