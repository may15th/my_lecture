from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
import requests
from .serializers import WeatherSerializer
from .models import Weather
# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city ='Seoul,KR'
    url =  f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    
    response = requests.get(url).json()
    
    return Response(response)

@api_view(['GET'])
def save_data(request):
    api_key = settings.API_KEY
    city ='Seoul,KR'
    url =  f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    
    response = requests.get(url).json()
    
    for li in response.get("list"):
        save_data = {
            'dt_txt': li.get('dt_txt'),
            'temp': li.get('main').get('temp'),
            'feels_like': li.get('main').get('feels_like'),
        }
        
        #저장하기 위해 데이터를 포장, 유효성 검사 위해 바로 create하지 않음.
        serializer = WeatherSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    # 저장완료 메시지        
    # 홈페이지에 데이터 저장완료됨을 보내줌
    return JsonResponse({ 'message' : 'okay' })
    

# DB 저장된 전체 데이터 조회
@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all()    # Weather.objects.all()는 데이터 아니야. 쿼리셋일 뿐.
    #serializer가 응답할 수 있는 형태(json)으로 포장하는 역할 함.
    serializer =WeatherSerializer(weathers, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def hot_weathers(request):
    #1. 데이터를 필터링하고, 필터링된 것을 모두 포장
    weathers = Weather.objects.all()
    hot_weathers = []
    for weather in weathers:
        # 섭씨 - 켈빈 - 273.15
        tmp = round(weather.temp - 273.15,2)
        if tmp >20:
            hot_weathers.append(weather)
    
    serializer = WeatherSerializer(hot_weathers, many=True)
    return Response(serializer.data)

    #2. serializer자체에서 필터링 하는 경우.


    pass

    
    