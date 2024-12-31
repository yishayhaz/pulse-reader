import json
import numpy as np
from scipy.signal import find_peaks

def write(data: list, fps: int):
  with open('data.json', 'w') as f:
    json.dump({
      'data': data,
      'fps': fps
    }, f)
    f.close()

def read():
  with open('data.json', 'r') as f:
    data = json.load(f)
    f.close()
    return data['data'], data['fps']

def count_peaks(data: list[int]):
  peaks, properties = find_peaks(
    data,
    prominence=0.025,
    distance=22
  )
  return peaks

def pulse(data: list, fps: int):
  length = len(data)
  r, g, b = np.array(data).T

  r_peaks, g_peaks, b_peaks = count_peaks(r), count_peaks(g), count_peaks(b)

  avg_peaks = len(b_peaks) #(len(r_peaks) + len(g_peaks) + len(b_peaks)) / 3

  seconds = length / fps

  return avg_peaks / seconds * 60