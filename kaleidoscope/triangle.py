"""Module qui gère des triangles"""

from math import cos, sin
from random import randint
from collections import namedtuple
from module_svg import Point

Triangle = namedtuple('Triangle', 'a b c')


def triangle_aleatoire(frontiere_x, frontiere_y):
    return Triangle(
        Point(randint(frontiere_x[0], frontiere_x[1]),
              randint(frontiere_y[0], frontiere_y[1])),
        Point(randint(frontiere_x[0], frontiere_x[1]),
              randint(frontiere_y[0], frontiere_y[1])),
        Point(randint(frontiere_x[0], frontiere_x[1]),
              randint(frontiere_y[0], frontiere_y[1])),
    )


def tourne_triangle_autour(triangle, centre, angle):
    a_x = (triangle.a.x - centre.x) * cos(angle) - (triangle.a.y - centre.y) * sin(angle) + centre.x
    b_x = (triangle.b.x - centre.x) * cos(angle) - (triangle.b.y - centre.y) * sin(angle) + centre.x
    c_x = (triangle.c.x - centre.x) * cos(angle) - (triangle.c.y - centre.y) * sin(angle) + centre.x

    a_y = (triangle.a.x - centre.x) * sin(angle) + (triangle.a.y - centre.y) * cos(angle) + centre.y
    b_y = (triangle.b.x - centre.x) * sin(angle) + (triangle.b.y - centre.y) * cos(angle) + centre.y
    c_y = (triangle.c.x - centre.x) * sin(angle) + (triangle.c.y - centre.y) * cos(angle) + centre.y

    return Triangle(
        Point(int(a_x), int(a_y)),
        Point(int(b_x), int(b_y)),
        Point(int(c_x), int(c_y)),
    )
