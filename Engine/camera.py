from .settings import *


class Camera:
    def __init__(self, position, yaw, pitch):
        self.position = glm.vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)

        self.__up = glm.vec3(0, 1, 0)
        self.__right = glm.vec3(1, 0, 0)
        self.__forward = glm.vec3(0, 0, -1)

        self.matrix_projection = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.matrix_view = glm.mat4()

    def update(self):
        self.update_vectors()
        self.update_view_matrix()

    def update_view_matrix(self):
        self.matrix_view = glm.lookAt(self.position, self.position + self.__forward, self.__up)

    def update_vectors(self):
        self.__forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.__forward.y = glm.sin(self.pitch)
        self.__forward.z = glm.sin(self.yaw) * glm.cos(self.pitch)

        self.__forward = glm.normalize(self.__forward)
        self.__right = glm.normalize(glm.cross(self.__forward, glm.vec3(0, 1, 0)))
        self.__up = glm.normalize(glm.cross(self.__right, self.__forward))

    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, -PITCH_MAX, PITCH_MAX)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def move_left(self, velocity):
        self.position -= self.__right * velocity

    def move_right(self, velocity):
        self.position += self.__right * velocity

    def move_up(self, velocity):
        self.position += self.__up * velocity

    def move_down(self, velocity):
        self.position -= self.__up * velocity

    def move_forward(self, velocity):
        self.position += self.__forward * velocity

    def move_back(self, velocity):
        self.position -= self.__forward * velocity
