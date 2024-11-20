#Please read it 
#커밋 풀 시 .env파일 추가 --> 토큰 값

# 모듈 가져오기
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from PIL import Image
import requests
import re

#///////////////////////////////////////////////////////////////////#


#실행시 정사각형 이미지로 하세요!!!!!!!


#///////////////////////////////////////////////////////////////////#

# 봇 기본 설정(디스코드 챗봇)

load_dotenv()
token = os.getenv("TOKEN") # .env 파일에서 토큰 값 가져오기

intents = discord.Intents.all()  # 기본 인텐트 설정
intents.members = True  # 서버 멤버 목록을 읽을 수 있는 인텐트 설정

bot = commands.Bot(command_prefix='!', intents=intents)

#///////////////////////////////////////////////////////////////////#
# 고정 변수

model = load_model('models/emotion_detection_model_15epochs.h5')
file_path = 'imgsave/saved_image.jpg'
folder_path = 'imgsave'

#///////////////////////////////////////////////////////////////////#

    #사진 전처리
    #감정 분석

def imgsave(url):
    try:
        # URL에서 이미지 데이터 가져오기
        response = requests.get(url)
        response.raise_for_status()

        # 이미지 파일로 저장
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"이미지가 {file_path}에 저장되었습니다.")
    except Exception as e:
        print(f"이미지 저장 중 오류 발생: {e}")

def imgdel():
    try:
        # 폴더 내의 모든 이미지 파일 삭제
        [os.remove(os.path.join(folder_path, file)) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg'))]

        print("이미지 파일을 모두 삭제했습니다.")
    except Exception as e:
        print(f"이미지 삭제 중 오류 발생: {e}")

def imgprocessing(url):
    try:
        img = Image.open(url).convert('L')  # 흑백으로 변환
        
        img = img.resize((48, 48))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # 배치 차원 추가
        img_array /= 255.0  # 이미지를 0~1 범위로 정규화
        print('분석중')
        return img_array
    
    
    except:
        print('실패')

def imgpredict(X):
    predict = model.predict(X)
    return predict


def display():
    a = str(imgpredict(imgprocessing(file_path))).replace(' ',',')
    a = a.replace('[','')
    a = a.replace(']','')
    a = re.sub(',+', ',', a)
    a = [float(item) for item in a.split(',')]
    # (화남, 공포, 행복, 중립, 슬픔, 놀람)
    return a

#///////////////////////////////////////////////////////////////////#


@bot.event #로그인 확인
async def on_ready(): 
    print('im online')



@bot.event 
async def on_message(message):
    if message.author == bot.user:
            return
    if message.content == "안녕":
        await message.channel.send("안녕하세요")
    await bot.process_commands(message)
    if message.attachments and not message.content.startswith('!image'):
        image_url = message.attachments[0].url
        print(image_url) #test 용
        await message.channel.send("잠시만 기다려 주세요")
        imgsave(image_url) #이미지 저장

        a = display()
        # (화남, 공포, 행복, 중립, 슬픔, 놀람)
        angry = int(a[0]*100)
        fearful = int(a[1]*100)
        happy = int(a[2]*100)
        neutral = int(a[3]*100)
        sad = int(a[4]*100)
        surprised = int(a[5]*100)
        await message.channel.send(f"당신의 얼굴은 분노{angry}%, 두려움{fearful}%, 행복{happy}%, 중립{neutral}%, 슬픔{sad}%, 놀라움{surprised}% 입니다")

        imgdel() #이미지 죽임
        

#///////////////////////////////////////////////////////////////////#
bot.run(token)