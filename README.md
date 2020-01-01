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