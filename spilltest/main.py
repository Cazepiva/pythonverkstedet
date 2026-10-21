import asyncio
import random
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fang myntene!")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

player = pygame.Rect(100, 100, 40, 40)
coin = pygame.Rect(400, 250, 25, 25)

score = 0
speed = 5


async def main():
    global score

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= speed
        if keys[pygame.K_RIGHT]:
            player.x += speed
        if keys[pygame.K_UP]:
            player.y -= speed
        if keys[pygame.K_DOWN]:
            player.y += speed

        player.clamp_ip(screen.get_rect())

        if player.colliderect(coin):
            score += 1
            coin.x = random.randint(0, WIDTH - 25)
            coin.y = random.randint(0, HEIGHT - 25)

        screen.fill((190, 230, 190))

        pygame.draw.rect(screen, (255, 140, 50), player)
        pygame.draw.circle(screen, (255, 215, 0), coin.center, 13)

        score_text = font.render(
            f"Poeng: {score}", True, (30, 30, 30)
        )
        screen.blit(score_text, (20, 20))

        pygame.display.flip()
        clock.tick(60)

        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
