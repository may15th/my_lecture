from django.shortcuts import render
import matplotlib.pyplot as plt
# io : 입출력 연산을 위한 python 표준 라이브러리
# BytestIO: 이진 데이터를 다루기 위한 버퍼 제공
# 버퍼: 임시 저장 공간.
# 파일 시스템과 유사하지만, 실제로 파일로 만들지 않고 메모리 단에서 작업할 수 있다.
from io import BytesIO

# base 64: 텍스트 <-> 이진데이터를 변환할 수 있는 모듈
import base64

# 그래프를 그려볼 것이다!
def index(request):
    x = [1,2,3,4]
    y = [2,4,8,16]

    # 다른 view함수에서
    # 다시 그리는 경우를 대비하여, 초기화를 진행
    plt.clf()

    plt.plot(x,y)
    plt.title("graph")
    plt.ylabel('y label')
    plt.xlabel('x label')

    # 비어있는 버퍼를 생성
    buffer = BytesIO()

    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    #버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹페이지에
    # url형식(주소형식)으로 만들어진 문자열을 생성


    context = {
        # chart_image : 저장된 이미지의 경로
        'chart_image': f'data:image/png;base64, {image_base64}'
    }

    return render(request, "index.html", context)

import pandas as pd
csv_path = 'firstapp/data/austin_weather.csv'

def example(request):
    df = pd.read_csv(csv_path)
    context = {
        'df' : df,
    }
    return render(request, 'example.html', context)