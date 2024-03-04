from .settings import *


class ShaderProgram:
    def __init__(self, app) -> None:
        self.app = app
        self.ctx = app.ctx
        self.player = app.player

        # region Shaders
        self.quad = self.get_program(shader_name = "quad")
        # endregion

        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        self.quad['matrix_projection'].write(self.player.matrix_projection)
        self.quad['matrix_model'].write(glm.mat4())

    def update(self):
        self.quad['matrix_view'].write(self.player.matrix_view)

    def get_program(self, shader_name: str):
        with open(f"Engine/shaders/{shader_name}.vert", 'r') as file:
            vector_shader = file.read()

        with open(f"Engine/shaders/{shader_name}.frag", 'r') as file:
            fragment_shader = file.read()

        program = self.ctx.program(
            vertex_shader = vector_shader,
            fragment_shader = fragment_shader
        )
        return program
