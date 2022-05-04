import sys
import numpy as np
from tkinter import *
from math import *


class Figure:
    def __init__(self):
        self.coordinates = [[-50, 50, 50],
                            [-50, 50, -50],
                            [50, 50, -50],
                            [50, 50, 50],
                            [-50, -50, 50],
                            [-50, -50, -50],
                            [50, -50, -50],
                            [50, -50, 50]]

        self.x = 0
        self.y = 0

        self.EPS = lambda d: d * pi / 180

        # counter-clockwise rotation about the X axis
        self.ROT_X = lambda x: self.matrix_transpose([[1, 0, 0],
                                                      [0, cos(x), -sin(x)],
                                                      [0, sin(x), cos(x)]])

        # counter-clockwise rotation about the Y axis
        self.ROT_Y = lambda y: self.matrix_transpose([[cos(y), 0, sin(y)],
                                                      [0, 1, 0],
                                                      [-sin(y), 0, cos(y)]])

        # counter-clockwise rotation about the Z axis
        self.ROT_Z = lambda z: self.matrix_transpose([[cos(z), sin(z), 0],
                                                      [-sin(z), cos(z), 0],
                                                      [0, 0, 1]])

        self.root = Tk()
        self.root.title('figure move')
        self.root.geometry('+0+0')

        """Створення полтна на якому буде малюватись фігура"""
        self.canvas = Canvas(self.root, width=500, height=500, background='white')
        self.canvas.pack(fill=BOTH, expand=YES)

        """Оголошення обробників подій мишки"""
        self.canvas.bind("<Button-1>", self.clicked)
        self.canvas.bind("<B1-Motion>", self.motion)
        self.canvas.bind("<Configure>", self.resize)
        self.canvas.bind_all('<MouseWheel>', self.wheel)

    def matrix_multiplication(self, mat1, mat2):
        """Множення двох матриць mat1 на mat2"""
        return np.matmul(mat1, mat2)

    def translate(self, x, y, dx, dy):
        """Зсув кооординати на крок"""
        return x + dx, y + dy

    def matrix_transpose(self, matrix):
        """Трансопнування матриці"""
        return np.array(matrix).T

    def clicked(self, event):
        """Save current mouse position."""
        print(event.x, event.y)
        self.x = event.x
        self.y = event.y

    def motion(self, event):
        step_x = self.x - event.x
        step_y = self.y - event.y

        self.coordinates = self.matrix_multiplication(self.coordinates, self.ROT_X(self.EPS(-step_y)))

        self.coordinates = self.matrix_multiplication(self.coordinates, self.ROT_Y(self.EPS(step_x)))

        self.draw()
        self.clicked(event)

    def wheel(self, event):
        """Map mouse wheel displacements to rotations about Z axis."""
        self.coordinates = self.matrix_multiplication(self.coordinates, self.ROT_Z(self.EPS(event.delta / 120)))
        self.draw()

    def resize(self, event):
        """Redraw the tetrahedron, in case of a window change due to user resizing it."""
        self.draw()

    def draw(self, visible='blue', invisible='red'):
        w, h = self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2
        self.canvas.delete(ALL)
        figure = self.coordinates
        size = len(self.coordinates)

        for m in range(size):
            for n in range(m + 1, size):
                if (m, n) not in [(0, 2), (0, 5), (0, 6), (0, 7), (1, 3), (1, 4), (1, 6), (1, 7),
                                  (2, 4), (2, 5), (2, 7), (3, 4), (3, 5), (3, 6), (4, 6), (5, 7)]:
                    if figure[m][0] > 0 and figure[m][1] < 0 and figure[m][2] > 0:
                        """Перебір координат, малювання ліній між ними і їх зсув від центру координат"""
                        self.canvas.create_line(self.translate(figure[m][0], figure[m][1], w, h),
                                                self.translate(figure[n][0], figure[n][1], w, h),
                                                fill=invisible, dash=(5, 2))
                    else:
                        self.canvas.create_line(self.translate(figure[m][0], figure[m][1], w, h),
                                                self.translate(figure[n][0], figure[n][1], w, h), fill=visible)

    def main(self):
        self.draw()
        mainloop()


if __name__ == '__main__':
    figure = Figure()
    sys.exit(figure.main())
