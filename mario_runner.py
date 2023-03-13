#Nomes:Matheus Guimaraes Liporace

import pygame
from sys import exit
from random import randint

def display_score():
    current_time=int(pygame.time.get_ticks()//1000) -start_time
    score_surf = test_font.render(f"Score:{current_time}",False,(64,64,64))
    score_rect = score_surf.get_rect(center =(400,50))
    screen.blit(score_surf,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=8
            if obstacle_rect.bottom == 450:
                screen.blit(goomba_surface,obstacle_rect)
            else:
                screen.blit(koopa_surf,obstacle_rect)
   
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return[]
def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):return False
    return True
def player_animation():
    global player_surf,player_index

    if player_rect.bottom <440:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index=0
        player_surf = player_walk[int(player_index)]

pygame.init()
altura = 800
largura = 600
screen=pygame.display.set_mode((altura,largura))
pygame.display.set_caption('Mario Runner')
clock= pygame.time.Clock()
game_active= False
test_font = pygame.font.Font('marioz/Pixeltype.ttf',50)
start_time=0
score= 0


#Ceu
sky_surface = pygame.image.load('marioz/mario_sky.png').convert_alpha()
sky_surface = pygame. transform. scale(sky_surface,(800,440)).convert_alpha()

#Chao
ground_surface = pygame.image.load('marioz/ground.png')
ground_surface = pygame. transform.scale(ground_surface,(800,160)).convert_alpha()

#Obstacles
goomba_walk1 = pygame.image.load('marioz/goomba.png').convert_alpha()
goomba_walk1 = pygame. transform. scale(goomba_walk1,(50,80)).convert_alpha()
goomba_walk2 = pygame.image.load('marioz/goomba2.png').convert_alpha()
goomba_walk2 = pygame. transform. scale(goomba_walk2,(50,80)).convert_alpha()
goomba_walk=[goomba_walk1,goomba_walk2]
goomba_walk_index=0
goomba_surface= goomba_walk[goomba_walk_index]



koopa_fly1 = pygame.image.load('marioz/koopa1.png').convert_alpha()
koopa_fly1 = pygame. transform. scale(koopa_fly1,(50,80)).convert_alpha()
koopa_fly2 = pygame.image.load('marioz/koopa2.png').convert_alpha()
koopa_fly2 = pygame. transform. scale(koopa_fly2,(50,80)).convert_alpha()
koopa_fly=[koopa_fly1,koopa_fly2]
koopa_fly_index=0
koopa_surf=koopa_fly[koopa_fly_index]

obstacle_rect_list=[] 


#Mario
player_walk1 = pygame.image.load('marioz/mario.png').convert_alpha()
player_walk1 = pygame. transform. scale(player_walk1,(50,100)).convert_alpha()
player_walk2 = pygame.image.load('marioz/mario1.png').convert_alpha()
player_walk2 = pygame. transform. scale(player_walk2,(80,130)).convert_alpha()
player_jump = pygame.image.load('marioz/mario_jump.png').convert_alpha()
player_jump = pygame. transform. scale(player_jump,(75,125)).convert_alpha()


player_walk=[player_walk1,player_walk2]
player_index = 0
player_surf= player_walk[player_index]
player_rect = player_surf.get_rect(topleft=(200,360))
player_gravity= 0

#Outro
player_end = pygame.image.load('marioz/mario_end.png').convert_alpha()
player_end= pygame. transform. scale(player_end,(300,300)).convert_alpha()
player_end_rect = player_end.get_rect(center=(altura/2,largura/2))
game_over_surf = test_font.render("GAME OVER!!",False,(255,255,255))
game_over_rect= game_over_surf.get_rect(center=(400,100))
restart_surf = test_font.render("Press R to restart game",False,(255,255,255))
restart_rect= restart_surf.get_rect(center=(400,550))

#Intro
player_start = pygame.image.load('marioz/mario_start.png').convert_alpha()
player_start= pygame. transform. scale(player_start,(300,300)).convert_alpha()
player_start_rect= player_start.get_rect(center=(altura/2,largura/2))
welcome_surf = test_font.render("Welcome to Mario Runner!",False,(255,255,255))
welcome_rect= welcome_surf.get_rect(center=(400,100))
start_surf = test_font.render("Press R to start running",False,(255,255,255))
start_rect= start_surf.get_rect(center=(400,550))

#Timer
obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,800)

goomba_animation_timer = pygame.USEREVENT+2
pygame.time.set_timer(goomba_animation_timer,200)

koopa_animation_timer = pygame.USEREVENT+3
pygame.time.set_timer(koopa_animation_timer,100)

#Sound

background_sound=  pygame.mixer.Sound('marioz/mario_song.mp3')
background_sound.play(loops=-1)
background_sound.set_volume(0.5)
jump_sound= pygame.mixer.Sound('marioz/mario_jump.mp3')
jump_sound.set_volume(0.5)


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE and player_rect.bottom>=440:
                    player_gravity =-20
                    jump_sound.play()
            if e.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(goomba_surface.get_rect(midbottom=(randint(900,1100),450)))
                else:
                    obstacle_rect_list.append(koopa_surf.get_rect(topleft=(randint(900,1100),170)))
            if e.type == goomba_animation_timer:
                if goomba_walk_index == 0:goomba_walk_index=1
                else: goomba_walk_index =0
                goomba_surface=goomba_walk[goomba_walk_index]
            if e.type == koopa_animation_timer:
                if koopa_fly_index == 0:koopa_fly_index=1
                else: koopa_fly_index =0
                koopa_surf=koopa_fly[koopa_fly_index]                
        else:
            if e.type == pygame.KEYDOWN and e.key ==pygame.K_r:
                game_active = True
                start_time = pygame.time.get_ticks()//1000
            
    if game_active:            
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,440))
        score=display_score()
        
        #Mario
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom>= 440:
            player_rect.bottom=440
        player_animation()
        screen.blit(player_surf,player_rect)

    
        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active= collisions(player_rect,obstacle_rect_list)
           
    
    else:
        screen.fill((94,129,162))
        #Intro
        if score==0:
            screen.blit(player_start,player_start_rect)
            screen.blit(welcome_surf,welcome_rect)
            screen.blit(start_surf,start_rect)
        #Outro  
        else:
            screen.blit(player_end,player_end_rect)
            screen.blit(game_over_surf,game_over_rect)
            screen.blit(restart_surf,restart_rect)
            obstacle_rect_list.clear()
            player_rect.topleft= (200,360)
            player_gravity=0
            score_message = test_font.render(f'Your Score:{score}',False,(255,255,255))
            score_message_rect = score_message.get_rect(center =(400,500))
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)
