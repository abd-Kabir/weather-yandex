from django.urls import path

from apps.weather.views import GetWeatherAPIView, WeatherByCityName

app_name = 'weather'
urlpatterns = [
    path('test/', GetWeatherAPIView.as_view(), name='test'),  # was created to test yandex API, no need to use it

    path('city/', WeatherByCityName.as_view(), name='weather_by_city'),
]
