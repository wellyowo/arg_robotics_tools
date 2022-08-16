# AUTOGENERATED! DO NOT EDIT! File to edit: ../05_random_map.ipynb.

# %% auto 0
__all__ = ['random_generate', 'sub_random_generate', 'draw_line']

# %% ../05_random_map.ipynb 4
from random import uniform
import matplotlib.pyplot as plt
import numpy as np

def random_generate(offset_x, offset_y, point_num, area_length_x, area_length_y):
    """
        generate random points with mutiple parameters.
        Args:
            offset_x : offset for x's range.
            offset_y : offset for y's range.
            point_num : number of points to generate.
            area_length_x : x's range for generate random points.
            area_length_y : y's range for generate random points.
        Returns:
            rand_point_x : list of random points' x coordinate.
            rand_point_y : list of random points' y coordinate.
    """
    rand_point_x = []
    rand_point_y = []
    rand_point_x = [(uniform(-area_length_x/2, area_length_x/2) + offset_x) for _ in range(point_num)]
    rand_point_y = [(uniform(-area_length_y/2, area_length_y/2) + offset_y) for _ in range(point_num)]
    return rand_point_x, rand_point_y

def sub_random_generate(offset_x, offset_y, point_num, area_length_x, area_length_y, sub_area_num, sub_offset_x, sub_offset_y):
    """
        generate random points with mutiple parameters, including sub_area_num and sub_offset.
        Args :
            offset_x : offset for x's range.
            offset_y : offset for y's range.
            point_num : number of points to generate.
            area_length_x : x's range for generate random points.
            area_length_y : y's range for generate random points.
            sub_area_num : 
            sub_offset_x : 
            sub_offset_y :
        Returns :
            rand_point_x : list of random points' x coordinate.
            rand_point_y : list of random points' y coordinate.
        Outputs : 
            output_point.txt : random points' x and y coordinate.
    """
    rand_point_x = []
    rand_point_y = []
    path = "output_point.txt"
    f = open(path, "w")
    for i in range(sub_area_num):
        generated_x = [(uniform(-area_length_x/2 + i*(area_length_x/sub_area_num)+sub_offset_x, -area_length_x/2 + (i+1)*(area_length_x/sub_area_num)-sub_offset_x)
            + offset_x) for _ in range(int(point_num/sub_area_num))]
        generated_y = [(uniform(-area_length_y/2+sub_offset_y, area_length_y/2-sub_offset_y) + offset_y) for _ in range(int(point_num/sub_area_num))]
        rand_point_x.extend(generated_x)
        rand_point_y.extend(generated_y)
        print("Area", i, ":", file=f)
        for j in range(int(point_num/sub_area_num)):
            print(generated_x[j], generated_y[j], file=f)
    f.close()
    return rand_point_x, rand_point_y

def draw_line(sub_area_num, x_min, x_increment, y_min, y_max):
    """
    draw straight line in a plot.
    Args:
        sub_area_num : number of area that separated by lines.
        x_min : where the line starts. 
        x_increment : distance of two lines.
        y_min : line's y lower coordinate.
        y_max : line's y upper coordinate.
    """
    
    for i in range(sub_area_num):
        plt.vlines(x_min, y_min, y_max, color='green')
        x_min += x_increment
    

