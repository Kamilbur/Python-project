import pygame

from settings import *


class Models:
    try:
        BARON_R_IMG = pygame.image.load(IMAGE_PATH + "baron_r.png")
        BARON_L_IMG = pygame.image.load(IMAGE_PATH + "baron_l.png")
        BARON_L_SQUAT_IMG = pygame.image.load(IMAGE_PATH + "baron_l_squat.png")
        BARON_R_SQUAT_IMG = pygame.image.load(IMAGE_PATH + "baron_r_squat.png")
        BARON_R_DAM_IMG = pygame.image.load(IMAGE_PATH+"baron_dam_r.png")
        BARON_L_DAM_IMG = pygame.image.load(IMAGE_PATH+"baron_dam_l.png")
        BARON_L_JUMPING_IMG = pygame.image.load(IMAGE_PATH + "baron_l_jumping.png")
        BARON_R_JUMPING_IMG = pygame.image.load(IMAGE_PATH + "baron_r_jumping.png")
        BARON_L_DAM_JUMPING_IMG = pygame.image.load(IMAGE_PATH + "baron_dam_l_jumping.png")
        BARON_R_DAM_JUMPING_IMG = pygame.image.load(IMAGE_PATH + "baron_dam_r_jumping.png")
        BARON_R_BRAKING_IMG = pygame.image.load(IMAGE_PATH + "baron_r_braking.png")
        BARON_L_BRAKING_IMG = pygame.image.load(IMAGE_PATH + "baron_l_braking.png")
        BARON_R_DAM_BRAKING_IMG = pygame.image.load(IMAGE_PATH + "baron_dam_r_braking.png")
        BARON_L_DAM_BRAKING_IMG = pygame.image.load(IMAGE_PATH + "baron_dam_l_braking.png")

        PLATFORM_IMG = pygame.image.load(IMAGE_PATH + "platform.png")
        BRIDGE_IMG = pygame.image.load(IMAGE_PATH + "bridge.png")
        BRIDGE_DAM = pygame.image.load(IMAGE_PATH + "bridge_dam.png")
        FOE_FLAG_IMG = pygame.image.load(IMAGE_PATH + "foe_flag.png")
        BARON_FLAG_IMG = pygame.image.load(IMAGE_PATH + "baron_flag.png")
        BULLET_IMG = pygame.image.load(IMAGE_PATH + "bullet.png")
        FOE_R_IMG = pygame.image.load(IMAGE_PATH + "foe_r.png")
        FOE_L_IMG = pygame.image.load(IMAGE_PATH + "foe_l.png")
        FOE_R_DAM_IMG = pygame.image.load(IMAGE_PATH + "foe_dam_r.png")
        FOE_L_DAM_IMG = pygame.image.load(IMAGE_PATH + "foe_dam_l.png")
        HEART_IMG = pygame.image.load(IMAGE_PATH + "heart.png")
        TOWER_IMG = pygame.image.load(IMAGE_PATH + "tower.png")
        COMPANION = pygame.image.load(IMAGE_PATH + "compan.png")
        COMPANION_DAM = pygame.image.load(IMAGE_PATH + "compan_dam.png")


        R_1 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_1.png")
        R_2 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_2.png")
        R_3 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_3.png")
        R_4 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_4.png")
        R_5 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_5.png")
        R_6 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_6.png")
        R_7 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_7.png")
        R_8 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_8.png")
        R_9 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_9.png")
        R_10 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_10.png")
        R_11 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_11.png")
        R_12 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_12.png")
        R_13 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_13.png")
        R_14 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_14.png")
        R_15 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_15.png")
        R_16 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_16.png")
        R_17 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_17.png")
        R_18 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_18.png")
        R_19 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_19.png")
        R_20 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_20.png")
        R_21 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_21.png")
        R_22 = pygame.image.load(BARON_RIGHT_ANIMATION_PATH + "r_22.png")

        L_1 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_1.png")
        L_2 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_2.png")
        L_3 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_3.png")
        L_4 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_4.png")
        L_5 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_5.png")
        L_6 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_6.png")
        L_7 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_7.png")
        L_8 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_8.png")
        L_9 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_9.png")
        L_10 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_10.png")
        L_11 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_11.png")
        L_12 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_12.png")
        L_13 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_13.png")
        L_14 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_14.png")
        L_15 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_15.png")
        L_16 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_16.png")
        L_17 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_17.png")
        L_18 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_18.png")
        L_19 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_19.png")
        L_20 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_20.png")
        L_21 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_21.png")
        L_22 = pygame.image.load(BARON_LEFT_ANIMATION_PATH + "l_22.png")

        FR_1 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "1_r.png")
        FR_2 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "2_r.png")
        FR_3 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "3_r.png")
        FR_4 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "4_r.png")
        FR_5 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "5_r.png")
        FR_6 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "6_r.png")
        FR_7 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "7_r.png")
        FR_8 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "8_r.png")
        FR_9 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "9_r.png")
        FR_10 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "10_r.png")
        FR_11 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "11_r.png")
        FR_12 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "12_r.png")
        FR_13 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "13_r.png")
        FR_14 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "14_r.png")
        FR_15 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "15_r.png")
        FR_16 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "16_r.png")
        FR_17 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "17_r.png")
        FR_18 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "18_r.png")
        FR_19 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "19_r.png")
        FR_20 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "20_r.png")
        FR_21 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "21_r.png")
        FR_22 = pygame.image.load(FOE_RIGHT_ANIMATION_PATH + "22_r.png")

        FL_1 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "1_l.png")
        FL_2 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "2_l.png")
        FL_3 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "3_l.png")
        FL_4 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "4_l.png")
        FL_5 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "5_l.png")
        FL_6 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "6_l.png")
        FL_7 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "7_l.png")
        FL_8 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "8_l.png")
        FL_9 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "9_l.png")
        FL_10 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "10_l.png")
        FL_11 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "11_l.png")
        FL_12 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "12_l.png")
        FL_13 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "13_l.png")
        FL_14 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "14_l.png")
        FL_15 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "15_l.png")
        FL_16 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "16_l.png")
        FL_17 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "17_l.png")
        FL_18 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "18_l.png")
        FL_19 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "19_l.png")
        FL_20 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "20_l.png")
        FL_21 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "21_l.png")
        FL_22 = pygame.image.load(FOE_LEFT_ANIMATION_PATH + "22_l.png")

    except IOError as er:
        print("I/O error in loading models: " + er.strerror)
