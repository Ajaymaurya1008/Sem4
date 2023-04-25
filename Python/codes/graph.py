import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
x = [2,5,7]
y = [4,7,9]
x2 = [15,21,23]
y2 = [15,75,36]

plt.title("First graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot(x,y, label = 'first',linewidth = 5)
plt.plot(x2,y2, label = 'second')
plt.legend()
plt.show()
