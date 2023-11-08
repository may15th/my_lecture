from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
import requests
from .serializers import DepositProductsSerializer,DepositOptionsSerializer
from .models import DepositProducts, DepositOptions


API_KEY = settings.API_KEY

# Create your views here.

# requests 모듈을 활용하여 정기예금 상품 목록 데이터를 가져와 정기예금 상품 목록과 옵션 목록을 DB에 저장 
@api_view(['GET'])
def index(request):
    # api_key = settings.API_KEY
    # city ='Seoul,KR'
    # url =  f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    
    # response = requests.get(url).json()
    
    # return Response(response)
    pass

@api_view(['GET'])
def save_deposit_products(request):
    pass

@api_view(['GET'])
def deposit_products(request):
    pass
# POST도 추가
@api_view(['GET','POST'])
def deposit_product_options(request):
    pass

@api_view(['GET'])
def top_rate(request):
    pass