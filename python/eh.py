#!/usr/bin/env python

import numpy as np
import math

def upper_plane_to_disk(x, y):
    x_disk = (2*x) / (x**2 + (1+y)**2)
    y_disk = (x**2+y**2-1) / (x**2 + (1+y)**2)
    return (x_disk, y_disk)

def upper_plane_to_disk_complex(z):
    if (z == -1.j):
        return 0. + 9999999.j
    return (z-1.j) / (z+1.j)

def make_linfractrans(a, b, c, d):
    return np.array([[a, b], [c, d]])

def make_point_reflection(x, y):
    return make_linfractrans(y, x, -1, -y)

def make_line_reflection(l1, l2):
    return make_linfractrans(-l2, -l1, 1, l2)

def make_line_reflection_end(l1, l2):
    return make_linfractrans(-1, -l1, 0, 1)

def apply_transformation(matrix, z):
    num = matrix[0][0]*z + matrix[0][1]
    den = matrix[1][0]*z + matrix[1][1]
    if (den == 0):
        return ("infty", "infty")
    return num / den


z0 = 0. + 0.j 
z1 = 1. + 0.j
z2 = 0. + 1.j 
z3 = -1. + 0.j 
z4 = 0. - 1.j
z5 = .1 + 0.j
z6 = 0. + .1j 
z7 = -.1 + 0.j 
z8 = 0. - .1j

z_arr = [z0, z1, z2, z3, z4, z5, z6, z7, z8]


def print_all_linfractranses(): 
  
    print("\nLINEAR FRACTIONAL TRANSFORMATIONS")
    
    ## z -> 2z
    print("\n\nz -> 2z\n")
    M = make_linfractrans(2, 0, 0, 1)
    for z in z_arr:
        print apply_transformation(M, z)


    ## z -> z/5
    print("\n\nz -> z/5\n")
    M = make_linfractrans(1, 0, 0, 5)
    for z in z_arr:
       print apply_transformation(M, z)


    ## z -> 2z + 1
    print("\n\nz -> 2z + 1\n")
    M = make_linfractrans(2, 1, 0, 1)
    for z in z_arr:
        print apply_transformation(M, z)


    ## z -> 2z + 1 / 5
    print("\n\nz -> 2z + 1 / 5\n")
    M = make_linfractrans(2, 1, 0, 5)
    for z in z_arr:
        print apply_transformation(M, z)


    ## z -> 2z + 1 / 3z
    print("\n\nz -> 2z + 1 / 3z\n")
    M = make_linfractrans(2, 1, 3, 0)
    for z in z_arr:
        print apply_transformation(M, z)


    ## z -> 2z + 1 / 3z + 5
    print("\n\nz -> 2z + 1 / 3z + 5\n")
    M = make_linfractrans(2, 1, 3, 5)
    for z in z_arr:
        print apply_transformation(M, z)



def print_all_point_reflections(): 
  
    print("\nPOINT REFLECTIONS")
    
    print("\n\nover 0. + 0.j\n")
    M = make_point_reflection(0., 0.)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))


    print("\n\nover 1. + 0.j\n")
    M = make_point_reflection(1., 0.)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))


    print("\n\nover 0. + 1.j\n")
    M = make_point_reflection(0., 1.)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))


    print("\n\nover -1. + 0.j\n")
    M = make_point_reflection(-1., 0.)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))


    print("\n\nover 0. - 1.j\n")
    M = make_point_reflection(0, -1.)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))


    print("\n\nover .1 + 0.j\n")
    M = make_point_reflection(.1, 0.)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))


    print("\n\nover 0. + .1j\n")
    M = make_point_reflection(0., .1)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))


    print("\n\nover -.1 + 0.j\n")
    M = make_point_reflection(-.1, 0.)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))


    print("\n\nover 0. - .1j\n")
    M = make_point_reflection(0, -.1)
    for z in z_arr:
        print str(z) + " --> " + str(upper_plane_to_disk_complex(z)) + " --> " + str(apply_transformation(M, upper_plane_to_disk_complex(z)))



#print_all_linfractranses()
#print_all_point_reflections()
print("\nPOINTS")
for z in z_arr: 
    print (z, upper_plane_to_disk_complex(z))

 

def check():
    print("\nPOINT REFLECTIONS")
    
    print("\n\nover .1 + 0.j\n")
    M = make_point_reflection(.1, 0.)
    for z in z_arr:
        print (math.sqrt(z.real**2 + z.imag**2) < 1)


    print("\n\nover 0. + .1j\n")
    M = make_point_reflection(0., .1)
    for z in z_arr:
        print (math.sqrt(z.real**2 + z.imag**2) < 1)


    print("\n\nover -.1 + 0.j\n")
    M = make_point_reflection(-.1, 0.)
    for z in z_arr:
        print (math.sqrt(z.real**2 + z.imag**2) < 1)


    print("\n\nover 0. - .1j\n")
    M = make_point_reflection(0, -.1)
    for z in z_arr:
        print (math.sqrt(z.real**2 + z.imag**2) < 1)

check()



