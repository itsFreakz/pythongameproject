import pygame

pygame.init()

#DISPLAY SIZE
WIDTH, HEIGHT = 1400, 810

#Window/Game Name
pygame.display.set_caption('2D Freakz Knight Adventure')

#CREATE THE PYGAME WINDOW
window = pygame.display.set_mode((WIDTH, HEIGHT))

#START MENU
def start_menu():
    font = pygame.font.SysFont('comicsans', 60)
    title = font.render('Freakz Knight Adventure', True, (255, 255, 255))

    font = pygame.font.SysFont('comicsans', 30)
    start_button = font.render('Start Game', True, (255, 255, 255))
    quit_button = font.render('Quit', True, (255, 255, 255))

    start_rect = start_button.get_rect(center=(WIDTH/2, HEIGHT/2))
    quit_rect = quit_button.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))

    # Load the background image
    background_image = pygame.image.load('sky.jpg')

    run = True
    while run:
        # Draw the background image
        window.blit(background_image, (0, 0))

        # Draw the other elements of the start menu
        window.blit(title, (WIDTH/2 - title.get_width()/2, 50))
        window.blit(start_button, start_rect)
        window.blit(quit_button, quit_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if start_rect.collidepoint(mouse_pos):
                    run = False
                    return

                if quit_rect.collidepoint(mouse_pos):
                    run = False
                    pygame.quit()
                    quit()

start_menu()