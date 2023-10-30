from rest_framework import serializers
from .models import Weather

# .Modelserializer 인 이유: 이미 models.py에서 지정된 필드 세 가지만 사용하기 때문.
# 만약에 따로 필드 지정한다면 그냥 .serializer 사용.
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
        