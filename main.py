import pygame, sys
pygame.init()
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
#fonts and text and location of text
font = pygame.font.Font('freesansbold.ttf', 32)

collision_detection_text = font.render("colliding", True, green, blue)

fps = str(int(clock.get_fps()))
fps_text = font.render(fps, True, green, blue)
fps_text_loc = (5, 5)

#collision
collide_teleport_time = 0
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

def player_movement(player_x,player_y,player_speed):
    keys = pygame.key.get_pressed()
    # collision_detection_text = font.render("No Collision", True, green, blue)
    # player_color = blue
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    return player_x, player_y

def collision_teleport_time(collision_index, player_rect, player_x, player_y, collide_teleport_time):
    player_y =+ 5
    collide_teleport_time = 0
    if player_rect.colliderect(tile_rect_list[collision_index]):
        player_x =+ 5
        collide_teleport_time = 0
        if player_rect.colliderect(tile_rect_list[collision_index]):
            player_y =- 15
            collide_teleport_time = 0
            if player_rect.colliderect(tile_rect_list[collision_index]):
                player_x =- 15
                collide_teleport_time = 0


def player_collision(player_rect,player_x,player_y, collision_tolerance,tile_rect_list, collision_index):
    # collision_detection_text = font.render("No Collision", True, green, blue)
    # player_color = green
    # collide_teleport_time =+ 0.01
    if abs(player_rect.top - tile_rect_list[collision_index].bottom) < collision_tolerance:
        player_y += collision_tolerance + 7
    if abs(player_rect.bottom - tile_rect_list[collision_index].top) < collision_tolerance:
        player_y -= collision_tolerance + 7
    if abs(player_rect.right - tile_rect_list[collision_index].left) < collision_tolerance:
        player_x -= collision_tolerance + 7
    if abs(player_rect.left - tile_rect_list[collision_index].right) < collision_tolerance:
        player_x += collision_tolerance + 7
    return player_x, player_y

def quit():
    pygame.quit()
    sys.exit()

def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, True, green, blue)
    return fps_text

def update_display():
    pygame.display.update()

def game_loop():
    global collide_teleport_time, collision_detection_text
    #player
    player_color = blue
    player_speed = 6
    player_x = 500
    player_y = 500
    player_rect = pygame.draw.rect(displaysurf, player_color, pygame.Rect(player_x, player_y, tile_size, tile_size))
    while game_state == 'tag':
        displaysurf.fill(black)
        update_fps()
        tiles(map1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        player_x, player_y = player_movement(player_x,player_y,player_speed)
        collision_indexes = player_rect.collidelistall(tile_rect_list)
        while len(collision_indexes) > 0:
            collision_index = collision_indexes[0]
            # player_x, player_y = player_collision(player_rect,player_x,player_y, collision_tolerance,tile_rect_list, collision_index)
            if abs(player_rect.top - tile_rect_list[collision_index].bottom) < collision_tolerance:
                player_y += collision_tolerance + 7
            if abs(player_rect.bottom - tile_rect_list[collision_index].top) < collision_tolerance:
                player_y -= collision_tolerance + 7
            if abs(player_rect.right - tile_rect_list[collision_index].left) < collision_tolerance:
                player_x -= collision_tolerance + 7
            if abs(player_rect.left - tile_rect_list[collision_index].right) < collision_tolerance:
                player_x += collision_tolerance + 7
            collision_indexes = player_rect.collidelistall(tile_rect_list)
        # if collide_teleport_time == 5:
        #     collision_teleport_time(collision_indexes, player_rect, player_x, player_y, collide_teleport_time)
        player_rect = pygame.draw.rect(displaysurf, player_color, pygame.Rect(player_x, player_y, tile_size, tile_size))
        displaysurf.blit(collision_detection_text, (fps_text_loc[0], fps_text_loc[1]+30))
        displaysurf.blit(fps_text, fps_text_loc)
        update_display()
        clock.tick(60)

if __name__ == '__main__':
    game_loop()