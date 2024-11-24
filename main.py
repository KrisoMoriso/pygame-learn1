import pygame as py
py.init()
screen = py.display.set_mode((1000, 1000))
py.display.set_caption('spirit')
clock = py.time.Clock()
#score
score = 0
test_font = py.font.Font('Pixeltype.ttf', 50)
score_surf = test_font.render(f'{score}', False, 'black')
score_rect = score_surf.get_rect(center=(500, 100))

background = py.Surface((1000, 1000))
background.fill((184, 136, 92))
ground = py.Surface((1000, 200))
ground.fill((75, 143, 50))
ground_rect = ground.get_rect(topleft=(0, 800))
#snail
snail = py.image.load('snail1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom=(800, 800))
#player
player = py.image.load('player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(200, 800))
player_gravity = 0
lock_mouse = False
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                if player_gravity == 0:
                    player_gravity += -15
    screen.blit(background, (0,0))
    screen.blit(ground, ground_rect)
    #player
    player_rect.bottom += player_gravity
    if player_rect.colliderect(ground_rect):
        player_gravity = 0
    else:
        player_gravity += 0.5
    screen.blit(player, player_rect)
    #mouse
    mouse_pos = py.mouse.get_pos()
    mouse_left = py.mouse.get_pressed()[0]
    a = clock.get_time()
    if mouse_left == True:
        a = clock.get_time()+200
    #snail
    snail_rect.left += -5
    if snail_rect.left < 0:
        snail_rect.left = 1000
        score += 1
    if snail_rect.collidepoint(mouse_pos) and mouse_left and mouse_lock:
        snail_rect.left = 1000
        score += 1
    if snail_rect.colliderect(player_rect):
        snail_rect.left = 1000
        score += -1
    screen.blit(snail, snail_rect)
    #score
    score_surf = test_font.render(f'{score}', False, 'black')
    screen.blit(score_surf, score_rect)
    #mouse
    if a > clock.get_time():
        mouse_lock = False
    else:
        mouse_lock = True



    py.display.update()
    clock.tick(165)