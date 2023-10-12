from rest_framework.response import Response
from rest_framework.views import APIView

from apps.weather.utils.integration import yandex_forecast


class GetWeatherAPIView(APIView):
    def get(self, request):
        response = yandex_forecast()
        return Response(response)
