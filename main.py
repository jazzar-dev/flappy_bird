import pygame

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy bird')


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load('/home/jazzar/Documents/cs/reach_cambridge/Reach_cambridge/Pygame'
                                         '/flappy_bird/assets/sprites/redbird-upflap.png'),
                       pygame.image.load('/home/jazzar/Documents/cs/reach_cambridge/Reach_cambridge/Pygame'
                                         '/flappy_bird/assets/sprites/redbird-midflap.png'),
                       pygame.image.load('/home/jazzar/Documents/cs/reach_cambridge/Reach_cambridge/Pygame'
                                         '/flappy_bird/assets/sprites/redbird-downflap.png')]
        self.image_num = 0
        self.image = self.images[self.image_num]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 6
        self.rect.y = SCREEN_HEIGHT // 2
        self.JUMP_DIST = 20

    def update(self):
        self.rect.y += 2.81
        self.image_num = (self.image_num + 1) % 3
        self.image = self.images[self.image_num]

    def up(self):
        if self.rect.y - self.JUMP_DIST - self.rect.size[1] + 10 > 0:
            self.rect.y -= self.JUMP_DIST


def main():
    img = pygame.image.load(
        '/home/jazzar/Documents/cs/reach_cambridge/Reach_cambridge/Pygame/flappy_bird/assets/sprites/background-day.png')
    img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    bird = Bird()
    bird_group = pygame.sprite.Group()
    bird_group.add(bird)

    clock = pygame.time.Clock()
    running = True
    while running:
        if clock.tick(10):
            screen.blit(img, (0, 0))
            bird_group.draw(screen)
            bird.update()
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.up()
                    bird.update()


if __name__ == '__main__':
    main()
    pygame.quit()
