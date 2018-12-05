from Classes import *
all_sprites_list = pygame.sprite.Group()
Alien_list = pygame.sprite.Group()
Asli_bullet_list = pygame.sprite.Group()
Nakli_bullet_list = pygame.sprite.Group()
Alien = Aliens()
Alien.time = timer()
Alien.initial_time = timer()
Alien_list.add(Alien)
all_sprites_list.add(Alien)
Shooter = Shoot()
all_sprites_list.add(Shooter)
clock = pygame.time.Clock()
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Shooter.x_velocity = -40
            elif event.key == pygame.K_d:
                Shooter.x_velocity = 40
            elif event.key == pygame.K_SPACE:
                h = Shooter.image.get_height()
                bullet = Asli_Bullet(
                    Shooter.rect.x+6, screen.get_height()-1.5*h)
                all_sprites_list.add(bullet)
                Asli_bullet_list.add(bullet)
            elif event.key == pygame.K_s:
                h = Shooter.image.get_height()
                bullet = Faltu_Bullet(
                    Shooter.rect.x+6, screen.get_height() - 1.5*h)
                all_sprites_list.add(bullet)
                Nakli_bullet_list.add(bullet)
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                Shooter.x_velocity = 0
        Shooter.rect.x += Shooter.x_velocity
        if Shooter.rect.x <= 0:
            Shooter.rect.x = 0
        elif Shooter.rect.x >= screen.get_width() - Shooter.image.get_width():
            Shooter.rect.x = screen.get_width() - Shooter.image.get_width()

    Alien.time = timer()
    if (Alien.time - Alien.initial_time) % 60 == 8:
        Alien_list.remove(Alien)
        all_sprites_list.remove(Alien)
    if (Alien.time - Alien.initial_time) % 60 >= 10:
        Alien = Aliens()
        Alien.initial_time = timer()
        Alien.time = timer()
        Alien_list.add(Alien)
        all_sprites_list.add(Alien)

    Asli_bullet_list.update()
    Nakli_bullet_list.update()
    for bullet in Asli_bullet_list:
        Alien_Hit = pygame.sprite.spritecollide(bullet, Alien_list, True)
        for Alien in Alien_Hit:
            Alien = Aliens()
            Alien.initial_time = timer()
            Alien.time = timer()
            Alien_list.add(Alien)
            all_sprites_list.add(Alien)
            Asli_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print("SCORE:"+str(score))

        if bullet.rect.y < -1:
            Asli_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    for bullet in Nakli_bullet_list:
        Ludaka_Hua_Alien = pygame.sprite.spritecollide(
            bullet, Alien_list, False)
        Ludak = pygame.sprite.Group()
        for t in Ludaka_Hua_Alien:
            Ludak.add(t)
            Asli_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
        Ludak.update()
        if bullet.rect.y < -1:
            Nakli_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    screen.fill((0, 0, 0))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
