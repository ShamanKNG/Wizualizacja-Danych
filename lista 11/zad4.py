import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



fig = plt.figure( figsize =( 10 , 6 ))
ax1 = fig.add_subplot( 231 , projection = '3d' )
ax2 = fig.add_subplot( 232 , projection = '3d' )
ax3 = fig.add_subplot( 233 , projection = '3d' )
ax4 = fig.add_subplot( 234 , projection = '3d' )
ax5 = fig.add_subplot( 235 , projection = '3d' )


_x = np.arange( 4 )
_y = np.arange( 5 )
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
ax1.set_title('1')
ax2.bar3d(x, y, bottom, width, depth, top,color='r',shade= False )
ax2.set_title('2')
ax3.bar3d(x, y, bottom, width, depth, top,color='pink' )
ax3.set_title('3')
ax4.bar3d(x, y, bottom, width, depth, top,color='olive',shade= False )
ax4.set_title('4')
ax5.bar3d(x, y, bottom, width, depth, top,color='cyan' )
ax5.set_title('5')
plt.show()