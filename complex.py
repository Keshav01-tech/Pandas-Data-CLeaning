import numpy as np 
import matplotlib.pyplot as plt
def z_function(x,y):
    return np.sin(5*x)*np.cos(5*y)/5
def derivative(x,y):
    return np.cos(5*x)*np.cos(5*y) ,-np.sin(5*x)*np.sin(5*x)
x = np.arange(-1,1,0.005)
y = np.arange(-1 ,1 ,0.005)
X,Y=np.meshgrid(x,y)
learning_rate = 0.01
z = z_function( X, Y)
current_pos = (0.7, 0.4 ,z_function(0.7,0.4))
for _ in range(1000):
       newx = current_pos[0] - learning_rate*derivative([current_pos[0],current_pos[1]])
       newy= z_function(newx)
ax= plt.subplot(projection ="3d")
ax.plot_surface(x,y,z ,cmap='Accent')
plt.show()