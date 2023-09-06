import pygame
import time
import random

from pygame import mixer

mixer.init()
mixer.music.set_volume(0.9)
mixer.music.load("ave_maria.wav.wav")
mixer.music.play()


WIDTH, HEIGHT = 1700, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dj's Star Dodge")

BG = pygame.transform.scale(pygame.image.load("space.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30

PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 45
STAR_VEL = 7

pygame.font.init()

FONT = pygame.font.SysFont("comicsans", 90)


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "green")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "green", player)

    for star in stars:
        pygame.draw.rect(WIN, "red", star)

    pygame.display.update()


def main():
    run = True
    

    player = pygame.Rect(100, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(100)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(30):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(300, star_add_increment - 70)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "green")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1500)
            br

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()