import numpy as np


class BaseMesh:
    def __init__(self):
        # OpenGL context
        self.ctx = None

        # Shader program
        self.program = None

        # Vertex buffer data type format: "3f 3f"
        self.vbo_format = None

        # Attributes names according to the format: ("in_position", "in_color")
        self.attributes = None

        # Vertex array object
        self.vao = None

    def get_vertex_data(self) -> np.array:
        pass

    def get_vao(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attributes)], skip_errors=True
        )
        return vao

    def render(self):
        self.vao.render()
