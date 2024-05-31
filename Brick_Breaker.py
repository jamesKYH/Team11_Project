import pygame
import sys
import itertools

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Brick Breaker")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# 폰트 설정
title_font = pygame.font.SysFont('comicsansms', 75)
instruction_font = pygame.font.SysFont('comicsansms', 35)

colors = [WHITE, YELLOW, GREEN, CYAN, MAGENTA, ORANGE, PURPLE]
color_cycle = itertools.cycle(colors)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def show_start_screen():
    screen.fill(BLUE)
    draw_text('Brick Breaker', title_font, next(color_cycle), screen, 400, 200)
    draw_text('Press any key to start', instruction_font, next(color_cycle), screen, 400, 400)
    pygame.display.flip()
    pygame.time.delay(500)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False
        screen.fill(BLUE)
        draw_text('Brick Breaker', title_font, next(color_cycle), screen, 400, 200)
        draw_text('Press any key to start', instruction_font, next(color_cycle), screen, 400, 400)
        pygame.display.flip()
        pygame.time.delay(500)

def show_game_over_screen():
    screen.fill(RED)
    draw_text('Game Over', title_font, next(color_cycle), screen, 400, 200)
    draw_text('Press any key to restart', instruction_font, next(color_cycle), screen, 400, 400)
    pygame.display.flip()
    pygame.time.delay(500)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False
        screen.fill(RED)
        draw_text('Game Over', title_font, next(color_cycle), screen, 400, 200)
        draw_text('Press any key to restart', instruction_font, next(color_cycle), screen, 400, 400)
        pygame.display.flip()
        pygame.time.delay(500)

# 패들 설정
paddle = pygame.Rect(375, 550, 50, 10)

# 공 설정
ball = pygame.Rect(390, 540, 10, 10)
ball_dx = 3
ball_dy = -3

# 벽돌 설정
stages = [5, 6, 7]  # 각 단계의 벽돌 행 수
current_stage = 0
brick_cols = 8
brick_offset_y = 50  # 벽돌을 아래로 내리는 오프셋 값

def create_bricks(rows):
    return [pygame.Rect(col * 100, row * 30 + brick_offset_y, 98, 28) for row in range(rows) for col in range(brick_cols)]

bricks = create_bricks(stages[current_stage])

# 목숨 설정
lives = 3

# 시작 화면 표시
show_start_screen()

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= 5
    if keys[pygame.K_RIGHT] and paddle.right < 800:
        paddle.right += 5
    
    # 공 이동
    ball.left += ball_dx
    ball.top += ball_dy

    # 벽과 충돌 처리
    if ball.left <= 0 or ball.right >= 800:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy
    
    # 패들과 충돌 처리
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # 벽돌과 충돌 처리
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_dy = -ball_dy
            bricks.remove(brick)

    # 모든 벽돌을 다 깼을 때 처리
    if not bricks:
        current_stage += 1
        if current_stage < len(stages):
            bricks = create_bricks(stages[current_stage])
            ball.left, ball.top = 390, 540
            ball_dx, ball_dy = 3, -3
        else:
            show_game_over_screen()
            running = False

    # 공이 바닥에 닿았을 때 처리
    if ball.top >= 600:
        lives -= 1
        if lives == 0:
            running = False
        else:
            ball.left, ball.top = 390, 540
            ball_dx, ball_dy = 3, -3

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)
    draw_text(f'Lives: {lives}', instruction_font, WHITE, screen, 60, 20)
    pygame.display.flip()

    # 프레임 속도 조절
    pygame.time.delay(30)

# 종료 화면 표시
show_game_over_screen()

# 게임 종료 처리
pygame.quit()
sys.exit()
