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

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 그리기
    screen.fill(BLACK)
    pygame.display.flip()

    # 프레임 속도 조절
    pygame.time.delay(30)

# 게임 종료 처리
pygame.quit()
sys.exit()
