import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("The Game")
square = pygame.Surface((50, 50))
square.fill('Purple')

myfont = pygame.font.Font('fonts/Minecraft.ttf', 40)


bg = pygame.image.load('background/bg.jpg')
player_speed = 5
player_x = 100
player_y = 140
jump_up = [pygame.image.load('jump_up/jump_1.png'),
           pygame.image.load('jump_up/jump_up_1.png'),
           pygame.image.load('jump_up/jump_up_2.png'),
           pygame.image.load('jump_up/jump_up_3.png'),
           pygame.image.load('jump_up/jump_up_4.png'),
           pygame.image.load('jump_down/jump_down_1.png'),
           pygame.image.load('jump_down/jump_down_2.png'),
           pygame.image.load('jump_down/jump_down_3.png'),
           pygame.image.load('jump_down/jump_down_4.png'),
           pygame.image.load('jump_down/jump_1.png')
           ]


walk_right = [pygame.image.load('player_right/afk1.png'),
              pygame.image.load('player_right/right_2.png'),
              pygame.image.load('player_right/right_3.png'),
              pygame.image.load('player_right/right_4.png')]

is_jump = False
jump_count = 7

player_jump_anim_count = 0
player_anim_count = 0
bg_x = 0

running = True
while running:

    keys = pygame.key.get_pressed()

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 400, 0))

    if keys[pygame.K_SPACE]:
        screen.blit(jump_up[player_jump_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True

    else:

        if jump_count >= -7:

            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1

        else:
            is_jump = False
            jump_count = 7

    if player_jump_anim_count == 9:
        player_jump_anim_count = 0
    else:
        player_jump_anim_count += 1

    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        bg_x -= 2
    elif keys[pygame.K_LEFT]:
        player_x -= player_speed
        bg_x += 2

    if player_x > 400:
        player_x = 0
    elif player_x < 0:
        player_x = 400

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    pygame.display.update()

    if bg_x == -400:
        bg_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(24)
