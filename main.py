import pygame

# Initialize PyGame
pygame.init()

# Create a display surface
screen = pygame.display.set_mode((800, 600))  # Width: 800px, Height: 600px
pygame.display.set_caption("Display Image Example")

# Load the image
image = pygame.image.load("name.png").convert_alpha()  # Use convert_alpha() for transparency

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    screen.fill((255, 255, 255))  # White background

    # Draw the image on the screen
    screen.blit(image, (100, 100))  # Position the image at (100, 100)

    # Update the display
    pygame.display.flip()

# Quit PyGame
pygame.quit()
