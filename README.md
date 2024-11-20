# Emotion_Bot

## CNN 감정인식 모델

> **동국대학교 사범대학 부속고등학교 인공지능 동아리**
>
> **개발기간 : 2023.06 ~ 2023.12**

## 주요기능

1. Discord를 이용하여 사용자로부터 안면 사진 입력
2. 학습된 CNN모델을 이용하여 5개의 감정을 확률로 수치화
3. 가장 높은 확률의 감정을 Discord를 이용하여 출력

## CNN 모델

**모델 구조:**

- Conv2D Layer (32 필터) - relu
- Conv2D Layer (64 필터) - relu
- MaxPooling2D Layer
- Dropout Layer
- Conv2D Layer (128 필터) - relu
- MaxPooling2D Layer
- Dropout Layer
- Conv2D Layer (256 필터) - relu
- MaxPooling2D Layer
- Dropout Layer
- Flatten Layer
- Dense Layer (512 뉴런) - relu
- Dropout Layer
- Dense Layer (6 뉴런) - softmax
- optimizer - adam, loss_f - categorical_crossentropy

**학습 데이터:** [Kaggle Emotion Detection Dataset](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer) 

**성능: 80%**

---



<div align=center> 
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
<br>
<img src="https://img.shields.io/badge/discord-5865F2?style=flat&logo=discord&logoColor=white">  
</div>
