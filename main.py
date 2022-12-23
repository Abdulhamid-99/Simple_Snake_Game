import sys

import pygame

import random
import time

# Initialize pygame
pygame.init()

# Set the width and height of the screen
screen_width = 200
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Snake Game')

# Set the dimensions of the snake
snake_block = 10
snake_speed = 30

# Set the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the font style
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Create a function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, blue, [x[0], x[1], snake_block, snake_block])


# Create a function to display the score
def show_score(choice, color, font, size):
    score = font.render("Score: " + str(score_value), True, color)
    screen.blit(score, [0, 0])


# Create a function to display the game over message
def game_over():
    my_font = pygame.font.SysFont('times new roman', 45)
    game_over_surface = my_font.render('Your Score is: ' + str(score_value), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Create the snake
snake_list = []
snake_length = 1

# Set the initial position of the snake
snake_x = 100
snake_y = 100

# Set the initial direction of the snake
snake_direction = 'right'

# Set the initial score to 0
score_value = 0

# Set the initial position of the food
food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# Set the game clock
clock = pygame.time.Clock()

# Run the game loop
while True:
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = 'up'
            if event.key == pygame.K_DOWN:
                snake_direction = 'down'
            if event.key == pygame.K_LEFT:
                snake_direction = 'left'
            if event.key == pygame.K_RIGHT:
                snake_direction = 'right'

                # Update the position of the snake based on the direction
            if snake_direction == 'up':
                snake_y -= snake_block
            if snake_direction == 'down':
                snake_y += snake_block
            if snake_direction == 'left':
                snake_x -= snake_block
            if snake_direction == 'right':
                snake_x += snake_block

                # Check if the snake has collided with the walls of the screen
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over()

                # Add the new position of the snake to the snake list
            snake_head = []
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_list.append(snake_head)

            # Check if the snake has eaten the food
            if snake_x == food_x and snake_y == food_y:
                # Generate a new piece of food in a random location
                food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
                food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
                snake_length += 1
                score_value += 1

            # If the snake has grown too long, remove the oldest piece
            if len(snake_list) > snake_length:
                del snake_list[0]

            # Check if the snake has collided with itself
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_over()

            # Fill the screen with the black color
            screen.fill(black)

            # Draw the snake and the food
            our_snake(snake_block, snake_list)
            pygame.draw.rect(screen, white, [food_x, food_y, snake_block, snake_block])

            # Display the score
            show_score(1, white, score_font, 20)

            # Update the display
            pygame.display.update()

            # Set the frame rate
            clock.tick(snake_speed)

