import numpy as np
import matplotlib.pyplot as plt

def draw_chart(data: list):
    r, g, b = np.array(data).T

    # Normalize the channels
    r = (r - np.min(r)) / (np.max(r) - np.min(r))
    g = (g - np.min(g)) / (np.max(g) - np.min(g))
    b = (b - np.min(b)) / (np.max(b) - np.min(b))

    # plt.plot(r, color='r', label='Red channel')
    plt.plot(g, color='g', label='Green channel')
    plt.plot(b, color='b', label='Blue channel')

    #show plt and a grid
    plt.legend()
    plt.grid()
    plt.show(block=False)