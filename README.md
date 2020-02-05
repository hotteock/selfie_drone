# selfie_drone

1. 프로젝트 시작 (12/31 ~)

2. 프로젝트 목표 : 셀피 드론 (Hover Camera)

3. 재료 : 라즈베리파이3+, webcam(마소 hd3000), 틸트/팬 모터, 드론

4. 계획
   1. 라즈베리파이 + 웹캠 + 틸트/팬 모터 를 통해 얼굴 추적 + 모터 제어
   
   2. 라즈베리파이 + 드론 제어
   
   3. 두 기능 합본
   
5. 참고 자료
   1. https://mangastorytelling.tistory.com/entry/%EB%B9%B5%ED%98%95%EC%9D%98-%EA%B0%9C%EB%B0%9C%EB%8F%84%EC%83%81%EA%B5%AD-%EC%96%BC%EA%B5%B4-%EC%9D%B8%EC%8B%9D-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%84%B1%EB%8A%A5-%EB%B9%84%EA%B5%90-Python-Deep-Learning
   
   python 얼굴 인식 알고리즘 비교 => OpenCV DNN face detector
   
6. 진행상황

  (12/31) https://github.com/kairess/face_detection_comparison

  OpenCV DNN face detector 코드와 훈련된 모델을 이용했다. 라즈베리파이에서 실행해본 결과 1 fps 정도의 속도를 얻을 수 있었다. 개선이 필요하다.

  또한 꼭 얼굴인식을 해야 할까 하는 생각이 들었다. 영상에서 일정 포인트를 기준으로 트래킹 해서 모터를 조작하고 이를 발전 시켜 드론 제어에 포함한다면 되지 않을까?

  (1/1) 서보모터 2개 + 팬틸트 모듈 주문.
  
  (1/2) yoloface 실행 해 본 결과 DNN과 비교 하여 빠르지 않았음. 
  
  https://towardsdatascience.com/real-time-face-recognition-with-cpu-983d35cc3ec5
  
  Ultra-light face detector라고 하는 오픈소스를 찾았다. 이것을 시도 해볼 예정 (dlib 설치가 오래걸린다.)
  
  (1/3) 서보모터 동작 확인, 파이 카메라 동작 확인 (but 파이 카메라는 웹캠과 비슷해 보인다. 이전의 코드에서 똑같은 fps 확인)
  
  어제의 ultra-light face detector는 onnc모델을 이용한 것 이었다. 라즈베리파이에서 onnc 동작이 잘 되지 않는것 같다.
  
  (1/6) 파이 카메라 모듈 - haar cascade 얼굴인식 (10fps) (640x480)
                        - opencv dnn detection (2.4fps) (640x480 / (200,200)
                        
  
  대략 5fps 정도를 얻고 싶은데 어떤 방법을 이용해야 할지 모르겠다. opencv dnn을 같은 모델을 사용하면서 여러 설정값을 조정해 볼 생각
  
  (1/7) 프레임을 읽어들이는 VideoCapture(0)를 queue를 사용하여 가속화 할 수 있다고 하여 그 라이브러리를 사용해 보았다. 하지만 다 처리하지 못하는것 같다.
  
  queue 사이즈를 줄이던지 아니면 detection 처리 자체를 병렬롤 해야할까?
  
  (1/10) mobilenet v2 + ssd 를 베이스로한 face detection 의 성능이 10fps 이상이 나오는 데모 영상을 접할 수 있었다. face 데이터셋을 구해서 tf-slim으로 학습시켜보자.
  
  윈도우에서 학습시키기 위해 사전작업 (tensorflow 설치)
  
  (2/5) WIDER 데이터셋을 Google vision API를 활용하여 정류하여 tfrecord를 만들고 이를 구글 Ai platform에서 트레이닝을 시켰다.
  
  트레이닝된 결과물을 바탕으로 Outfput_inference_graph.pb 폴더에 체크포인트 파일을 만들었다.