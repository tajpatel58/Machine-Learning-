from cost_func import cost_func
import numpy as np
from main import X,Y,lambd

def cost(p):
    return cost_func(X,Y,p,lambd)[0]