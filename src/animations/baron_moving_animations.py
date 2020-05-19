from models import Models
from basic.direction import Direction


class AnimationModels:

    def __init__(self):
        self.current_model = (Direction.RIGHT, 1)
        self.models_list = {(Direction.RIGHT, 0): Models.R_1,
                            (Direction.RIGHT, 1): Models.R_2,
                            (Direction.RIGHT, 2): Models.R_3,
                            (Direction.RIGHT, 3): Models.R_4,
                            (Direction.RIGHT, 4): Models.R_5,
                            (Direction.RIGHT, 5): Models.R_6,
                            (Direction.RIGHT, 6): Models.R_7,
                            (Direction.RIGHT, 7): Models.R_8,
                            (Direction.RIGHT, 8): Models.R_9,
                            (Direction.RIGHT, 9): Models.R_10,
                            (Direction.RIGHT, 10): Models.R_11,
                            (Direction.RIGHT, 11): Models.R_12,
                            (Direction.RIGHT, 12): Models.R_13,
                            (Direction.RIGHT, 13): Models.R_14,
                            (Direction.RIGHT, 14): Models.R_15,
                            (Direction.RIGHT, 15): Models.R_16,
                            (Direction.RIGHT, 16): Models.R_17,
                            (Direction.RIGHT, 17): Models.R_18,
                            (Direction.RIGHT, 18): Models.R_19,
                            (Direction.RIGHT, 19): Models.R_20,
                            (Direction.RIGHT, 20): Models.R_21,
                            (Direction.RIGHT, 21): Models.R_22,
                            (Direction.LEFT, 0): Models.L_1,
                            (Direction.LEFT, 1): Models.L_2,
                            (Direction.LEFT, 2): Models.L_3,
                            (Direction.LEFT, 3): Models.L_4,
                            (Direction.LEFT, 4): Models.L_5,
                            (Direction.LEFT, 5): Models.L_6,
                            (Direction.LEFT, 6): Models.L_7,
                            (Direction.LEFT, 7): Models.L_8,
                            (Direction.LEFT, 8): Models.L_9,
                            (Direction.LEFT, 9): Models.L_10,
                            (Direction.LEFT, 10): Models.L_11,
                            (Direction.LEFT, 11): Models.L_12,
                            (Direction.LEFT, 12): Models.L_13,
                            (Direction.LEFT, 13): Models.L_14,
                            (Direction.LEFT, 14): Models.L_15,
                            (Direction.LEFT, 15): Models.L_16,
                            (Direction.LEFT, 16): Models.L_17,
                            (Direction.LEFT, 17): Models.L_18,
                            (Direction.LEFT, 18): Models.L_19,
                            (Direction.LEFT, 19): Models.L_20,
                            (Direction.LEFT, 20): Models.L_21,
                            (Direction.LEFT, 21): Models.L_22}