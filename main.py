#token kod: 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

import pygame

pygame.init()

FPS = 60
WIN_HEIGHT = 500
WIN_WIDTH = 800
BAR_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
BAR_HEIGHT = 75
BAR_WIDTH = 20
VEL = 10
BALL_SIZE = 12

LEFT_BAR = pygame.Surface((BAR_WIDTH, BAR_HEIGHT))
RIGHT_BAR = pygame.Surface((BAR_WIDTH, BAR_HEIGHT))
BALL = pygame.Surface((BALL_SIZE, BALL_SIZE))

HEALTH_FONT = pygame.font.SysFont('comicsans', 25)
PLAYER_FONT = pygame.font.SysFont('comicsans', 30)

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Ping-pong") #Caption set

def draw_winner(text):
    draw_text = PLAYER_FONT.render(text,1,BAR_COLOR)
    WIN.blit(draw_text, (WIN_WIDTH/2 - draw_text.get_width()/2, WIN_HEIGHT/2-draw_text.get_height() /2))
    pygame.display.flip()
    pygame.time.delay(5000)

def draw_window(right_bar, left_bar, ball, right_health, left_health):
    WIN.fill(BG_COLOR)

    WIN.blit(RIGHT_BAR, (right_bar.x, right_bar.y))
    RIGHT_BAR.fill(BAR_COLOR)

    WIN.blit(LEFT_BAR, (left_bar.x, left_bar.y))
    LEFT_BAR.fill(BAR_COLOR)

    pygame.draw.rect(WIN, BAR_COLOR, (WIN_WIDTH // 2, 0, 2, WIN_HEIGHT))
    pygame.draw.ellipse(WIN, BAR_COLOR, ball)

    img = PLAYER_FONT.render('Player 1', True, BAR_COLOR)
    img2 = PLAYER_FONT.render('Player 2', True, BAR_COLOR)
    WIN.blit(img, (150, 20))
    WIN.blit(img2, (600, 20))

    right_health_text = HEALTH_FONT.render('Health:' + str(right_health), 1, BAR_COLOR)
    WIN.blit(right_health_text, (600,40))
    left_health_text = HEALTH_FONT.render('Health:' + str(left_health), 1, BAR_COLOR)
    WIN.blit(left_health_text, (150, 40))

    pygame.display.flip()

def left_move(keys_pressed, left_bar):
    if keys_pressed[pygame.K_w] and left_bar.y - VEL > 0:
        left_bar.y -= VEL
    if keys_pressed[pygame.K_s] and left_bar.y + BAR_HEIGHT + VEL < WIN_HEIGHT:
        left_bar.y += VEL


def right_move(keys_pressed, right_bar):
    if keys_pressed[pygame.K_UP] and right_bar.y - VEL > 0:
        right_bar.y -= VEL
    if keys_pressed[pygame.K_DOWN] and right_bar.y + BAR_HEIGHT + VEL < WIN_HEIGHT:
        right_bar.y += VEL


def main():
    right_bar = pygame.Rect(WIN_WIDTH - 20 - BAR_WIDTH, 250 - BAR_HEIGHT // 2, BAR_WIDTH, BAR_HEIGHT)
    left_bar = pygame.Rect(20, 250 - BAR_HEIGHT // 2, BAR_WIDTH, BAR_HEIGHT)

    right_health = 5
    left_health = 5

    ball = pygame.Rect(400, 250, BALL_SIZE, BALL_SIZE)
    ball_speed_x = 5
    ball_speed_y = 5

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        left_move(keys_pressed, left_bar)
        right_move(keys_pressed, right_bar)

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.top <= 0 or ball.bottom >= WIN_HEIGHT:
            ball_speed_y *= -1
        if ball.colliderect(left_bar) or ball.colliderect(right_bar):
            ball_speed_x *= -1
        elif ball.left <= 0:
            ball.x = 400
            ball.y = 250
            left_health = left_health - 1;
        elif ball.right >= WIN_WIDTH:
            ball.x = 400
            ball.y = 250
            right_health = right_health -1;

        winner_text = ""
        if right_health <= 0:
            winner_text = "Left WIN!"
        if left_health <= 0:
            winner_text= "Right WIN"
        if winner_text != "":
            draw_winner(winner_text)
            break

        draw_window(right_bar, left_bar, ball, right_health, left_health)

    pygame.quit()


if __name__ == "__main__":
    main()
