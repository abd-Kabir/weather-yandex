from django.urls import path

from apps.weather.views import GetWeatherAPIView, GetListCitiesAPIView

app_name = 'weather'
urlpatterns = [
    path('get/', GetWeatherAPIView.as_view(), name='get_weather'),
    path('cities/', GetListCitiesAPIView.as_view(), name='get_weather')
]
