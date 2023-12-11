import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections

cpu = collections.deque(np.zeros(10))
ram = collections.deque(np.zeros(10))

def my_function():
    cpu.popleft()
    cpu.append(psutil.cpu_percent(interval=1))
    ram.popleft()
    ram.append(psutil.virtual_memory().percent)

fig = plt.figure(figsize=(30,15), facecolor='#DEDEDE')
ax = plt.subplot(121)
ax1 = plt.subplot(122)
ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')

def animate(i):
    my_function()
    ax.clear()
    ax1.clear()
    ax.plot(cpu)
    #ax.scatter(len(cpu)-1, cpu[-1])
    #ax.text(len(cpu)-1, cpu[-1]+2, f"{cpu[-1]}%")
    ax.set_ylim(0,100)
    ax1.plot(ram)
    #ax1.scatter(len(ram)-1, ram[-1])
    #ax1.text(len(ram)-1, ram[-1]+2, f"{ram[-1]}%")
    ax1.set_ylim(0,100)

ani = FuncAnimation(fig, animate, interval=100)

plt.show()


