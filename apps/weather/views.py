from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.weather.utils.integration import yandex_forecast_coordination, yandex_forecast_city
from config.utils.api_exceptions import APIValidation


class GetWeatherAPIView(APIView):
    """
    This API was created for testing yandex integration
    :required query_params: lat, lon
    """

    def get(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        response = yandex_forecast_coordination(lat, lon)
        return Response(response)


class WeatherByCityName(APIView):
    """
    Get weather information by yandex integration with function - yandex_forecast_city()
    :required query_params: city
    """

    @method_decorator(cache_page(60 * 30))
    @method_decorator(vary_on_cookie)
    def get(self, request):
        city = request.query_params.get('city')
        if not city:
            raise APIValidation("City required in query params!", status_code=status.HTTP_400_BAD_REQUEST)
        weather_data = yandex_forecast_city(city)

        needed_data = {
            "city": city,
            "temp": weather_data.get('fact').get('temp'),
            "pressure_mm": weather_data.get('fact').get('pressure_mm'),
            "wind_speed": weather_data.get('fact').get('wind_speed'),
        }

        return Response(needed_data)
