# Importing necessary modules
# import pygame
# import sys
# from settings import SCREEN_WIDTH, SCREEN_HEIGHT
# from src.game import Game

# Initialize Pygame
# pygame.init()

# Main function
# def main():
#     # Set up the main window/screen
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Colony Game")

#     # Create a Game object
#     game = Game(screen)

#     # Main game loop
#     running = True
#     clock = pygame.time.Clock()
#     while running:
#         # Event handling
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Update game state
#         game.update()

#         # Drawing
#         game.draw()

#         # Update the display
#         pygame.display.flip()

#         # Cap the frame rate
#         clock.tick(60)

#     pygame.quit()
#     sys.exit()

# Entry point of the script
# if __name__ == "__main__":
#     main()
