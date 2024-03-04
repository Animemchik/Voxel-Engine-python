from numba import njit
import numpy as np
import glm
import math

# TODO: Make WINDOW_RESOLUTION resizeable
WINDOW_RESOLUTION = glm.vec2(1600, 900)

# region Camera settings
# TODO: Make FOV_DEG changeable
ASPECT_RATIO = WINDOW_RESOLUTION.x / WINDOW_RESOLUTION.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # Vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # Horizontal FOV
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)
# endregion

# region Player settings
# TODO: Make PLAYER_SPEED, PLAYER_ROT_SPEED, PLAYER_POS and MOUSE_SENSITIVITY changeable
PLAYER_SPEED = 0.005
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(0, 0, 1)
MOUSE_SENSITIVITY = 0.002
# endregion
