from numba import njit
import numpy as np
import glm
import math

# TODO: Make WINDOW_RESOLUTION resizeable
WINDOW_RESOLUTION = glm.vec2(1600, 900)

# region Chunk
CHUNK_SIZE = 16
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE ** 2
CHUNK_VOL = CHUNK_SIZE ** 3
# endregion

# region World
WORLD_WIDTH, WORLD_HEIGHT = 16, 16
WORLD_D = WORLD_WIDTH
WORLD_AREA = WORLD_WIDTH * WORLD_D
WORLD_VOL = WORLD_AREA * WORLD_HEIGHT

# world center
CENTER_XZ = WORLD_WIDTH * H_CHUNK_SIZE
CENTER_Y = WORLD_HEIGHT * H_CHUNK_SIZE
# endregion

# region Camera
# TODO: Make FOV_DEG changeable
ASPECT_RATIO = WINDOW_RESOLUTION.x / WINDOW_RESOLUTION.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)  # Vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)  # Horizontal FOV
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)
# endregion

# region Player
# TODO: Make PLAYER_SPEED, PLAYER_ROT_SPEED, PLAYER_POS and MOUSE_SENSITIVITY changeable
PLAYER_SPEED = 0.155
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_HEIGHT * CHUNK_SIZE, CENTER_XZ)
MOUSE_SENSITIVITY = 0.002
# endregion
