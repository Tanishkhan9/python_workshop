import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle and ball positions
paddle_a_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle_b_y = (HEIGHT - PADDLE_HEIGHT) // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 5, 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_b_y > 0:
        paddle_b_y -= 5
    if keys[pygame.K_DOWN] and paddle_b_y < HEIGHT - PADDLE_HEIGHT:
        paddle_b_y += 5
    if keys[pygame.K_w] and paddle_a_y > 0:
        paddle_a_y -= 5
    if keys[pygame.K_s] and paddle_a_y < HEIGHT - PADDLE_HEIGHT:
        paddle_a_y += 5

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= PADDLE_WIDTH and paddle_a_y < ball_y < paddle_a_y + PADDLE_HEIGHT) or \
       (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle_b_y < ball_y < paddle_b_y + PADDLE_HEIGHT):
        ball_speed_x *= -1

    # Reset ball if it goes out of bounds
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x *= -1

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (0, paddle_a_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle_b_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(60)
