import math
from display import *
from matrix import *

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
   # normalize(light[0])
   # normalize(normal)
   # normalize(view)
    amb = calculate_ambient(ambient, areflect)
   # print("amb:")
    #print(amb)
    diff = calculate_diffuse(light, dreflect, normal)
    spec = calculate_specular(light, sreflect, view, normal)
    vals = []
    for x in range(3):
        vals.append(amb[x] + diff[x] + spec[x])
    #limit_color(vals)
    return limit_color(vals)
    

def calculate_ambient(alight, areflect):
    #a: ambient light(0-255)
    #ka = constant of ambient reflection (0-1). Ambient = a * ka
    new_mat = []
    for x in range(3):
        new_mat.append(int(alight[x] * areflect[x]))
    #print("amb mat:")
    #print(limit_color(new_mat))
    return limit_color(new_mat)
    #return [0,0,0]

def calculate_diffuse(light, dreflect, normal):
    dot_prod = dot_product(normalize(light[0]), normalize(normal))
    new_mat = []
    for x in range(3):
        #new_mat.append(light[1][x] * dreflect[x] * dot_prod)
        new_mat.append(int(light[1][x] * dreflect[x] * dot_prod))
    #print("dif mat:")
    #print(new_mat)
    return limit_color(new_mat)
    #return [0,0,0]

def calculate_specular(light, sreflect, view, normal):
    normalize(normal)
    dot_prod1 = 2 * dot_product(normalize(normal), normalize(light[0]))
    prod = []
    for x in range(3):
        prod.append((dot_prod1 * normalize(normal)[x]) - normalize(light[0])[x])
    dot_prod2 = dot_product(prod, normalize(view))
    new_mat = []
    for x in range(3):
        new_mat.append(int(light[1][x] * sreflect[x] * (dot_prod2 ** SPECULAR_EXP)))
    return limit_color(new_mat)
    #return [0,0,0]

def limit_color(color):
    for x in range(3):
        if(color[x] <0):
            color[x] = 0
        if(color[x] > 255):
            color[x] = 255
    return color

#vector functions
def normalize(vector):
    denom = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    for x in range(3):
        vector[x] /=  denom
    return vector

def dot_product(a, b):
    prod = a[0] * b[0] + a[1]*b[1] + a[2]*b[2]
    return prod

def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
