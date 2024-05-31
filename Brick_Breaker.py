import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Brick Breaker")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# 패들 설정
paddle = pygame.Rect(375, 550, 50, 10)

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

    # 화면 그리기
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.display.flip()

    # 프레임 속도 조절
    pygame.time.delay(30)

# 게임 종료 처리
pygame.quit()
sys.exit()
