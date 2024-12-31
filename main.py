from read_video import read_video
from utils import read, write, pulse
from draw_chart import draw_chart

action = input("Write (w) or press any key to read:\n")

data = []
fps = 0

if action == 'w':
  path = input("Video path:\n")
  print("Reading video...")
  data, fps = read_video(path)
  print("FPS is " + str(fps))
  print("Writing data...")
  write(data, fps)

if action != 'w':
  print("Reading data...")
  data, fps = read()

print("Drawing chart...")
draw_chart(data)

print("Heart rate is " + str(pulse(data, fps)) + " BPM")
input("Press any key to exit")