# Ping Pong Game
#
# Author: Marco Breton
#
# Description: A simple game of Ping Pong using Python and pygame.
#


import pygame
import pygame.font
import random

# Initialize game
pygame.init()

# Font
font = pygame.font.Font(None, 36)

# Difficulty levels
EASY = 1
MEDIUM = 2
HARD = 3

# Menu button rectangles
easy_button_rect = None
medium_button_rect = None
hard_button_rect = None

# Display the menu
def display_menu(window):
    window.fill((0, 0, 0))

    # Difficulty level buttons
    easy_button = font.render("Easy", True, (255, 255, 255))
    medium_button = font.render("Medium", True, (255, 255, 255))
    hard_button = font.render("Hard", True, (255, 255, 255))

    # Button positions
    button_width = 100
    button_height = 50
    button_x = (window_width - button_width) // 2

    # Button rectangles
    global easy_button_rect, medium_button_rect, hard_button_rect
    
    easy_button_rect = easy_button.get_rect()
    easy_button_rect.topleft = (button_x, 200)
    
    medium_button_rect = medium_button.get_rect()
    medium_button_rect.topleft = (button_x, 300)
    
    hard_button_rect = hard_button.get_rect()
    hard_button_rect.topleft = (button_x, 400)

    # Blit buttons
    window.blit(easy_button, easy_button_rect)
    window.blit(medium_button, medium_button_rect)
    window.blit(hard_button, hard_button_rect)

# Display the scores
def display_scores():
    score_text = font.render(f"{player1_score} : {player2_score}", True, (255, 255, 255))
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 50))

# Display the game over screen
def display_game_over():
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (window_width // 2, window_height // 2)
    window.blit(game_over_text, game_over_rect)

    # Display final scores
    final_scores_text = font.render(f"Final Scores: {player1_score} : {player2_score}", True, (255, 255, 255))
    final_scores_rect = final_scores_text.get_rect()
    final_scores_rect.center = (window_width // 2, window_height // 2 + 50)
    window.blit(final_scores_text, final_scores_rect)

    # Restart and quit instructions
    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    restart_rect = restart_text.get_rect()
    restart_rect.center = (window_width // 2, window_height // 2 + 100)
    window.blit(restart_text, restart_rect)

    quit_text = font.render("Press Q to Quit", True, (255, 255, 255))
    quit_rect = quit_text.get_rect()
    quit_rect.center = (window_width // 2, window_height // 2 + 150)
    window.blit(quit_text, quit_rect)

# Game window setup
window_width = 1600
window_height = 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong Game")

# Paddle and ball properties
paddle_width = 10
paddle_height = 100
ball_radius = 10
paddle_speed = 1
ball_speed = 1  # Ball speed

# Create paddles
left_paddle = pygame.Rect(50, window_height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(window_width - 50 - paddle_width, window_height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Create the ball
ball = pygame.Rect(window_width // 2 - ball_radius, window_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# Variables
player1_score = 0
player2_score = 0

# Display the menu
selected_level = None
display_menu(window)
menu_running = True

# Game loop for the menu
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False

        # Check mouse clicks and select difficulty
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_button_rect.collidepoint(event.pos):
                selected_level = EASY
            elif medium_button_rect.collidepoint(event.pos):
                selected_level = MEDIUM
            elif hard_button_rect.collidepoint(event.pos):
                selected_level = HARD

    # Check if difficulty has been selected
    if selected_level is not None:
        # Player selected, exit the menu
        menu_running = False

    pygame.display.flip()

# Main game loop
game_over = False
running = True

# Initialize ball speed based on difficulty
if selected_level == EASY:
    ball_speed = 1
elif selected_level == MEDIUM:
    ball_speed = 2
elif selected_level == HARD:
    ball_speed = 3

# Ball direction and speed
ball_speed_x = random.choice((1, -1)) * ball_speed
ball_speed_y = random.choice((1, -1)) * ball_speed

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Get player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            left_paddle.y -= paddle_speed
        if keys[pygame.K_DOWN]:
            left_paddle.y += paddle_speed

        # AI for the right paddle
        if right_paddle.centery < ball.centery:
            right_paddle.y += paddle_speed
        if right_paddle.centery > ball.centery:
            right_paddle.y -= paddle_speed

        # Move the ball and check collisions
        ball.move_ip(ball_speed_x, ball_speed_y)

        if ball.top <= 0 or ball.bottom >= window_height:
            ball_speed_y = -ball_speed_y

        # Check ball boundaries
        if ball.left < 0:
            # Player 2 scores a point
            player2_score += 1
            # Reset ball
            ball.center = (window_width // 2, window_height // 2)
            ball_speed_x = abs(ball_speed_x) * random.choice((1, -1))
            ball_speed_y = abs(ball_speed_y) * random.choice((1, -1))

        if ball.right > window_width:
            # Player 1 scores a point
            player1_score += 1
            # Reset ball
            ball.center = (window_width // 2, window_height // 2)
            ball_speed_x = abs(ball_speed_x) * random.choice((1, -1))
            ball_speed_y = abs(ball_speed_y) * random.choice((1, -1))

        # Ball-paddle collision
        if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x = -ball_speed_x
            ball_speed_y = random.choice((1, -1)) * ball_speed

        # Check paddle boundaries
        if left_paddle.top < 0:
            left_paddle.top = 0
        if left_paddle.bottom > window_height:
            left_paddle.bottom = window_height
        if right_paddle.top < 0:
            right_paddle.top = 0
        if right_paddle.bottom > window_height:
            right_paddle.bottom = window_height

        # Ensure ball stays within boundaries
        if ball.top < 0:
            ball.top = 0
            ball_speed_y = -ball_speed_y
        if ball.bottom > window_height:
            ball.bottom = window_height
            ball_speed_y = -ball_speed_y

        # Game over condition
        if player1_score >= 7 or player2_score >= 7:
            game_over = True

    # Clear the screen
    window.fill((0, 0, 0))

    if not game_over:
        # Draw paddles and ball
        pygame.draw.rect(window, (255, 255, 255), left_paddle)
        pygame.draw.rect(window, (255, 255, 255), right_paddle)
        pygame.draw.ellipse(window, (255, 255, 255), ball)

        # Display scores
        display_scores()
    else:
        # Game over screen
        display_game_over()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart the game
                    player1_score = 0
                    player2_score = 0
                    game_over = False
                    ball_speed_x = random.choice((1, -1)) * ball_speed
                    ball_speed_y = random.choice((1, -1)) * ball_speed

                elif event.key == pygame.K_q:
                    # Quit the game
                    running = False

    pygame.display.flip()

pygame.quit()
