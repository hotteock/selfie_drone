from imutils.video import WebcamVideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2, time

# load model
model_path = 'opencv_face_detector_uint8.pb'
config_path = 'opencv_face_detector.pbtxt'
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

conf_threshold = 0.7

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100,
	help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1,
	help="Whether or not frames should be displayed")
args = vars(ap.parse_args())

# initialize video source, default 0 (webcam)
video_path = 'videos/RollerCoasters.mp4'
cap = WebcamVideoStream(src=0).start()

frame_count, tt = 0, 0
fps = FPS().start()

while fps._numFrames < args["num_frames"]:
  img = cap.read()
  img = imutils.resize(img, width=300)

  # prepare input
  result_img = img.copy()
  h, w, _ = result_img.shape
  blob = cv2.dnn.blobFromImage(result_img, 1.0, (300, 300), [104, 117, 123], False, False)
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
      cv2.rectangle(result_img, (x1, y1), (x2, y2), (255, 255, 255), int(round(h/150)), cv2.LINE_AA)
      cv2.putText(result_img, '%.2f%%' % (confidence * 100.), (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

  # inference time
  fps.update()
  cv2.putText(result_img, 'FPS(dnn): %.2f' % (fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

  # visualize
  if args["display"] > 0:
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

fps.stop()
cap.release()
cv2.destroyAllWindows()
