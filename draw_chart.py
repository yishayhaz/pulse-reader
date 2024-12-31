import numpy as np
import matplotlib.pyplot as plt

def draw_chart(data: list):
    r, g, b = np.array(data).T

    plt.plot(r / 255, color='r', label='Red channel')
    plt.plot(g / 255, color='g', label='Green channel')
    plt.plot(b / 255, color='b', label='Blue channel')

    #show plt and a grid
    plt.legend()
    plt.grid()
    plt.show(block=False)