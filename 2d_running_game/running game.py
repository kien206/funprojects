import pygame
from sys import exit
from random import randint
import pygame.image

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    text_surf = font.render('Score: ' + str(current_time), False, (64, 64, 64)).convert()
    text_rect = text_surf.get_rect(center=(400, 50))
    screen.blit(text_surf, text_rect)
    return current_time

pygame.init()

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail, obstacle_rect)
            else:
                screen.blit(fly, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():

    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]
    # play walking animation if player is on the floor
    # display the jump surface when the player jump (not on the floor)

screen = pygame.display.set_mode((800, 450))
pygame.display.flip()
pygame.display.set_caption('Game lon')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# text_surf = font.render('First game', False, (64, 64, 64)).convert()
# text_rect = text_surf.get_rect(center=(400, 50))

# player
player = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player, player2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(100, 300))
# vẽ cái rect quanh player để đặt player
player_gravity = 0

# snail
snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom=(700, 300))
snail2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail, snail2]
snail_frames_index = 0
snail_surf = snail_frames[snail_frames_index]

# fly
fly = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
fly2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly, fly2]
fly_frames_index = 0
fly_surf = fly_frames[fly_frames_index]

obstacle_rect_list = []

# Intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

intro_text_surf = font.render('Pixel Runner', False, (66, 135, 200))
intro_text_rect = intro_text_surf.get_rect(center=(400, 80))

game_message = font.render('Press SPACE to start', False, (66, 135, 200))
game_message_rect = game_message.get_rect(center=(400, 350))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

            '''if player_rect.collidepoint(event.pos):
                pass'''
        if game_active:
            if player_rect.bottom == 300:
                if event.type == pygame.KEYUP:  # phat hien khi nao bam nut
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_gravity = -20
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)
            # if event.type == pygame.KEYDOWN: # phat hien khi nao tha nut
            # pass
        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail.get_rect(midbottom=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(snail.get_rect(midbottom=(randint(900, 1100), 200)))

            if event.type == snail_animation_timer:
                if snail_frames_index == 0:
                    snail_frames_index = 1
                else:
                    snail_frames_index = 0
                snail_surf = snail_frames[snail_frames_index]

            if event.type == fly_animation_timer:
                if fly_frames_index == 0:
                    fly_frames_index = 1
                else:
                    fly_frames_index = 0
                fly_surf = fly_frames[fly_frames_index]

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        # pygame.draw.rect(screen, '#c0e8ec', text_rect, 6)
        # pygame.draw.rect(screen, '#c0e8ec', text_rect, 0, 10)
        # pygame.draw.ellipse(screen, 'Yellow', pygame.Rect(650,50, 100, 100))
        score = display_score()

        # screen.blit(text_surf, text_rect)
        '''screen.blit(snail, snail_rect)
        snail_rect.x -= 5

        if snail_rect.right <= -50:
            snail_rect.left = 800'''
        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        keys = pygame.key.get_pressed()

        # collision
        game_active = collision(player_rect, obstacle_rect_list)
        '''mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint(mouse_pos):
            print(pygame.mouse.get_pressed())'''
    else:
        screen.fill((66, 227, 245))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = font.render("Your score: " + str(score), False, (66, 135, 200))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(intro_text_surf, intro_text_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
    # tell the while loop not to run faster than 60fps
