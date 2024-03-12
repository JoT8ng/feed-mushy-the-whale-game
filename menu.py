import pygame
import os

def show_title_screen(screen, clock):
    title_font = pygame.font.Font(os.path.join("fonts", "PressStart2P.ttf"), 36)
    start_font = pygame.font.Font(os.path.join("fonts", "PressStart2P.ttf"), 24)
    keys_font = pygame.font.Font(os.path.join("fonts", "PressStart2P.ttf"), 12)
    title_text = title_font.render("Feed Mushy the Whale!", True, (237, 223, 124))
    start_text = start_font.render("Press Enter to Start", True, (255, 255, 255))
    keys_text = keys_font.render("Use 'W 'A' 'S' 'D' keys on your keyboard to move", True, (255, 255, 255))

    # Load sound
    start_sfx = pygame.mixer.Sound("assets/sound/mixkit-unlock-new-item-game-notification-254.wav")

    title_screen_running = True

    while title_screen_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_sfx.play()
                    title_screen_running = False

        screen.fill((67, 129, 142))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 200))
        screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, 400))
        screen.blit(keys_text, (screen.get_width() // 2 - keys_text.get_width() // 2, 600))

        pygame.display.update()
        clock.tick(30)
