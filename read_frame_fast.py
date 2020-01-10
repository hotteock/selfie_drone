import cv2
import sys
from threading import Thread
from queue import Queue

class FileVideoStream:
  def __init__(self, queueSize=128):
    self.stream = cv2.VideoCapture(0)
    self.stopped = False

    self.Q = Queue(maxsize=queueSize)

  def start(self):
    t = Thread(target=self.update, args=())
    t.daemon = True
    t.start()
    return self

  def update(self):
    while True:
      if self.stopped:
        return

      if not self.Q.full():
        (grabbed, frame) = self.stream.read()
        if not grabbed:
          self.stop()
          return

        self.Q.put(frame)

  def read(self):
    return self.Q.get()

  def more(self):
    return self.Q.qsize() >0

  def stop(self):
    self.stopped = True