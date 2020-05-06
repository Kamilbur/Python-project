from character import Character
import basic as bs
from models import Models
from settings import *


class Foe(Character):
    def __init__(self, img, x, y, level):
        super().__init__(img, bs.Point(x, y), level)
        self.foe_health = 3
        self.immortality_timer = 0
        self.reload_timer = 0
        self.bullets = FOE_BULLETS_PER_BURST

    def take_hit(self):
        self.foe_health -= 1
        self.immortality_timer = IMMORTALITY_TIME
        if(self.direction is bs.Direction.LEFT):
            self.image = Models.FOE_L_DAM_IMG
        else:
            self.image = Models.FOE_R_DAM_IMG

    def shoot(self):
        if (self.direction is bs.Direction.RIGHT):
            bullet_position = bs.Point(self.rect.x + 18, self.rect.y)
            bullet_velocity = bs.Point(15, 0)
            self.world.shoot(bullet_position, bullet_velocity)
        else:
            bullet_position = bs.Point(self.rect.x - 18, self.rect.y)
            bullet_velocity = bs.Point(-15, 0)
            self.world.shoot(bullet_position, bullet_velocity)

    def change_image(self):
        if(self.direction is bs.Direction.RIGHT):
            self.image = Models.FOE_R_IMG
        else:
            self.image = Models.FOE_L_IMG

    def reaches(self, hero_position):
        if(abs(hero_position.y - self.position.y) > CELL_SIZE*3/4):
            return False
        else:
            if(self.direction is bs.Direction.LEFT):
                return FOE_RANGE > self.position.x - hero_position.x > 0
            else:
                return 0 < self.position.x - hero_position.x > FOE_RANGE

    def reverse_direction(self):
        if(self.direction is bs.Direction.RIGHT):
            self.direction = bs.Direction.LEFT
        else:
            self.direction = bs.Direction.RIGHT

    def update(self):

        old_point = self.position
        if(self.direction is bs.Direction.LEFT):
            x_direction = -1

        else:
            x_direction = 1
        self.accelerate(x_direction * HORIZONTAL_ACCELERATION / 2, 0)
        if (not self.ground_detector.is_on_ground()):
            self.velocity.x = 0
            self.accelerate(-x_direction * HORIZONTAL_ACCELERATION / 2, 0)
            self.position.x -= 15 * x_direction
            self.position.y -= 15
            self.rect.x -= 15 * x_direction
            self.rect.y -= 15
            self.reverse_direction()

        super().update()

        if (old_point == self.position):
            self.reverse_direction()
