def method_name():
    import numpy as np
    def method_name():
        x = np.array(input("x: "))
        return x
    
    x = method_name()
    y = np.array([108, 70, 6])
    z = np.array([10, 3, 5])
    def new_func(x, y, z):
        c = np.concatenate((y,x))
        return c
    print ("x = ",x)
    print ("y = ", y)
    print ("c = ", new_func(x, y, z))
    return method_name, new_func, np, x, y, z

method_name, new_func, np, x, y, z = method_name()
