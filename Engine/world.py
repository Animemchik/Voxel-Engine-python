from .settings import *
from .world_objects import Chunk


class World:
    def __init__(self, app):
        self.app = app
        self.chunks: list[Chunk | None] = [None for _ in range(WORLD_VOL)]
        self.voxels = np.empty([WORLD_VOL, CHUNK_VOL], dtype = "uint8")
        self.build_chunks()
        self.build_chunk_mesh()

    def build_chunks(self):
        for x in range(WORLD_WIDTH):
            for y in range(WORLD_HEIGHT):
                for z in range(WORLD_D):
                    chunk = Chunk(self, position = (x, y, z))

                    chunk_index = x + WORLD_WIDTH * z + WORLD_AREA * y
                    self.chunks[chunk_index] = chunk

                    # put the chunk voxels in a separate array
                    self.voxels[chunk_index] = chunk.build_voxels()

                    # get pointer to voxels
                    chunk.voxels = self.voxels[chunk_index]

    def build_chunk_mesh(self):
        for chunk in self.chunks:
            chunk.build_mesh()

    def update(self):
        pass

    def render(self):
        for chunk in self.chunks:
            chunk.render()
