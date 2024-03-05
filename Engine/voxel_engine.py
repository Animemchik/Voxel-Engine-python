from .settings import *

import moderngl as mgl
import pygame as pg
import sys

from .shader_program import ShaderProgram
from .scene import Scene
from .player import Player
from .textures import Textures


class VoxelEngine:
    def __init__(self):
        pg.init()

        # region GL set attributes 
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)
        # endregion

        # region Pygame initialize
        pg.display.set_mode(WINDOW_RESOLUTION, flags = pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        self.ctx.enable(flags = mgl.DEPTH_TEST | mgl.CULL_FACE | pg.DOUBLEBUF)
        self.ctx.gc_mode = 'auto'

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        pg.event.set_grab(True)  # Mouse stays at the same pos
        pg.mouse.set_visible(False)  # Hides our mouse
        # endregion

        self.is_running = True

        self.shader_program = None
        self.scene = None
        self.player = None
        self.textures = None

        self.on_init()

    def on_init(self):
        self.textures = Textures(self)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    def update(self) -> None:
        self.player.update()
        self.shader_program.update()
        self.scene.update()

        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f"{self.clock.get_fps() : .1f}")

    def render(self) -> None:
        self.ctx.clear()
        self.scene.render()
        pg.display.flip()

    def handle_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self) -> None:
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit(0)
