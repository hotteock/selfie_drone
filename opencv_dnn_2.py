import cv2, time
import numpy as np
from imutils.video import FileVideoStream

# load model
model_path = 'opencv_face_detector_uint8.pb'
config_path = 'opencv_face_detector.pbtxt'
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

conf_threshold = 0.7

# initialize video source, default 0 (webcam)
#cap = cv2.VideoCapture(0)
fvs = FileVideoStream(0).start()
time.sleep(1.0)
frame_count, tt = 0, 0

while fvs.more():
  img = fvs.read()
  img = imutils.resize(img, width=450)
  img = np.dstack([img, img, img])

  frame_count += 1

  start_time = time.time()

  # prepare input
  h, w, _ = img.shape
  blob = cv2.dnn.blobFromImage(img, 1.0, (200, 200), [104, 117, 123], False, False)
  net.setInput(blob)

  # inference, find faces
  detections = net.forward()

  # postprocessing
  for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > conf_threshold:
      x1 = int(detections[0, 0, i, 3] * w)
      y1 = int(detections[0, 0, i, 4] * h)
      x2 = int(detections[0, 0, i, 5] * w)
      y2 = int(detections[0, 0, i, 6] * h)

      # draw rects
      cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), int(round(h/150)), cv2.LINE_AA)
      cv2.putText(img, '%.2f%%' % (confidence * 100.), (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

  # inference time
  tt += time.time() - start_time
  fps = frame_count / tt
  cv2.putText(img, 'FPS(dnn): %.2f' % (fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

  # visualize
  cv2.imshow('result', img)
  if cv2.waitKey(1) == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()
