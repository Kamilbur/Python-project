from collections import defaultdict

import pygame

from settings import *
import world_elements as we


class LevelLoader:
    """ Class handles input of level.

    Attributes:
        object_images(dict): Dictionary with keys being names of some level
                             objects f.e. 'foe' and images assigned to them.

    """

    def __init__(self, object_images):
        self.object_images = object_images

    def load_level(self, pathname):
        """ Load level from a file.

        Args:
            pathname: Path to a file.

        Returns:
            Level: The Level object filled with contents of a level
                encrypted in file, whose name is self.filename.
        """

        level = we.Level(pygame.sprite.Group(), pygame.sprite.Group(),
                         pygame.sprite.Group(), pygame.sprite.Group(),
                         pygame.sprite.Group(), pygame.sprite.Group(),
                         pygame.sprite.Group(), pygame.sprite.Group(),
                         pygame.sprite.Group())

        platforms = []
        platform_is_at = defaultdict(lambda: False)

        try:
            with open(pathname, 'r') as f:
                for i, line in enumerate(f):
                    for j in range(len(line)):
                        if (line[j] == '#'):
                            platforms += [
                                we.Platform(self.object_images['platform'],
                                            0.5 * j, i)]
                            platform_is_at[(platforms[-1].rect.x,
                                            platforms[-1].rect.y)] = True
                        if (line[j] == '$'):
                            level.flags.add(
                                [we.Flag(self.object_images['flag'],
                                         0.5 * j, i)])
                        if (line[j] == '*'):
                            level.foes.add(
                                [we.Foe(self.object_images['foe'], 0.5 * j, i,
                                        level)])
                        if (line[j] == '^'):
                            level.towers.add(
                                [we.Tower(self.object_images['tower'],
                                          0.5 * j, i)])

                        if (line[j] == '@'):
                            level.boss.add([we.Boss(self.object_images['boss'],
                                                    0.5 * j, i, level)])

                        if (line[j] == '&'):
                            bridge = we.Bridge(self.object_images['bridge'],
                                               0.5 * j, i)
                            level.bridges.add([bridge])

                            # Bridges are (for some time only) behaving like
                            # floor platform - treat them as one.
                            platform_is_at[(bridge.rect.x,
                                            bridge.rect.y)] = True
        except IOError as er:
            print(f"I/O error in loading level: " + er.strerror)

        def has_vertical_neighbors(plat):
            return (platform_is_at[(plat.rect.x, plat.rect.y - CELL_SIZE)] or
                    platform_is_at[(plat.rect.x, plat.rect.y + CELL_SIZE)])

        # def has_horizontal_neighbors(plat):
        #    return (platform_is_at[(plat.rect.x - CELL_SIZE, plat.rect.y)] or
        #            platform_is_at[(plat.rect.x + CELL_SIZE, plat.rect.y)])

        def is_wall(plat):
            return (has_vertical_neighbors(plat) and
                    not is_floor(plat))

        def is_floor(plat):
            return not platform_is_at[(plat.rect.x, plat.rect.y - CELL_SIZE)]

        # Platforms classification

        level.walls = pygame.sprite.Group(
            list(filter(lambda p: is_wall(p), platforms)))
        level.floors = pygame.sprite.Group(
            list(filter(lambda p: is_floor(p), platforms)))
        level.all_platforms = pygame.sprite.Group(platforms)

        return level
