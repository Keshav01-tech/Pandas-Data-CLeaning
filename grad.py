import numpy as np
import matplotlib.pyplot as plt
def y_value(x):
    return np.sin(x)
def y_derivative(x):
    return np.cos(x)
x= np.arange(-5, 5, 0.1)

y = y_value(x)
current_posstion = (1.5 , y_value(1.5))
larning_rate = 0.01
for _ in range(1000):
    newx = current_posstion[0] - larning_rate*y_derivative(current_posstion[0])
    newy= y_value(newx)
   
    current_posstion = (newx,newy)
    plt.plot(x,y)
    plt.scatter(current_posstion[0],current_posstion[1])

    plt.pause(0.001)
    plt.clf()
        
