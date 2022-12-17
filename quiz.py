import random
import pygame
##############################################################################################
# 게임에 필수 세팅 값
pygame.init() #초기화 

# 화면크기 설정
screen_width = 480    #가로 크기
screen_height = 600   #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("quiz") #게임 이름


# FPS
clock = pygame.time.Clock()
##############################################################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
background = pygame.image.load("/Users/chris/Desktop/pygame/background.png")
# 캐릭터 만들기
character = pygame.image.load("/Users/chris/Desktop/pygame/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height -character_height

# 이동 위치
to_x = 0
character_speed = 10


# 똥 만들기
ddong = pygame.image.load("/Users/chris/Desktop/pygame/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = 0
ddong_y_pos = 0
ddong_speed = 10

running = True 
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행 중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x
    ddong_y_pos += ddong_speed

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos)) # 적 그리기

    pygame.display.update()

    
# pygame 종료
pygame.quit()