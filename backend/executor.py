# a class for executing the instructions sent from API
import time
class Executor:
  def __init__(self, timeline):
    self.timeline = timeline

  def run(self):
    for i, frame in enumerate(self.timeline):
      print(i, frame)
      frame = 1 / 60
      time.sleep(frame)
