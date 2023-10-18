import pytest

from apps.weather.models import City


@pytest.mark.django_db
def test_create_city():
    city = City(name='New York', lat='40.7128', lon='-74.0060')
    city.save()

    # Check if the city was created in the database
    assert City.objects.count() == 1

    # Check if the attributes are correctly stored
    saved_city = City.objects.get(name='New York')
    assert saved_city.name == 'New York'
    assert saved_city.lat == '40.7128'
    assert saved_city.lon == '-74.0060'


def test_city_str_representation():
    city = City(name='Los Angeles', lat='34.0522', lon='-118.2437')
    assert str(city) == 'Los Angeles (lat: 34.0522, lon: -118.2437)'
