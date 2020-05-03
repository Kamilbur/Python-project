import pygame

import world_elements as we
from basic.point import Point
from models import Models
from settings import *


class Level:
    """

    Attributes:
        spawn:
        all_platforms:
        floors:
        walls:
        corners:
        foes:
        towers:
        bridges:
        flags:
        heroes:
        bullets:
    """

    def __init__(self, all_platforms, floors, walls, corners, foes, towers,
                 bridges, flags, heroes=None, spawn=None):
        self.spawn = spawn if (spawn) else we.Spawn()
        self.all_platforms = all_platforms
        self.floors = floors
        self.walls = walls
        self.corners = corners
        self.foes = foes
        self.towers = towers
        self.bridges = bridges
        self.flags = flags
        self.heroes = heroes if (heroes) else pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def shoot(self, start_position, velocity):
        self.bullets.add(we.Bullet(Models.BULLET_IMG, start_position,
                                   velocity))

    def move_bullets(self):
        self.bullets.update()
        for hero in self.heroes:
            if (pygame.sprite.spritecollide(hero, self.bullets, True)):
                hero.take_hit()

            if (hero.health == 0):
                hero.die()

        for foe in self.foes:
            foe.take_hit()

    def shoot_towers(self):
        for tower in self.towers:
            if (tower.reload_timer == 0):
                if (tower.bullets == 0):
                    tower.reload_timer = TOWER_RELOAD_TIME
                    tower.bullets = TOWER_BULLETS_PER_BURST
                else:
                    self.shoot(Point(tower.rect.x, tower.rect.y), Point(0, 3))
                    tower.bullets -= 1
                    tower.reload_timer = TOWER_TIME_BETWEEN_BULLETS_IN_BURST
            else:
                tower.reload_timer -= 1

    def follow_hero(self, dx):
        """ Move objects to follow hero.
        """
        self.all_platforms.update(dx)
        self.flags.update(dx)
        self.bridges.update(dx)
        self.towers.update(dx)

        for bullet in self.bullets:
            bullet.rect.x += dx

        for hero in self.heroes:
            hero.position += Point(dx, 0)

        for foe in self.foes:
            foe.position += Point(dx, 0)
