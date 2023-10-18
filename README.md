
#
Я хотел поблагодарить что вы дали мне шанс проявить себя. Надеюсь, я выполнил заданный таск правильно и я смогу стать
частью вашей команды)

# Start Project

Install all packages from **requirements.txt** file
`pip install -r requirements.txt`

Create **.env** file, you can get example from **.env.example** file

Run migrations:
`python manage.py makemigrations`
`python manage.py migrate`

Import data from **cities.csv** file to table _City_

Run Django application with command:
`python manage.py runserver`

Run Aiogram TG bot with command:
`python manage.py runtg`

## WeatherAPI
To get weather data use URL below:
`/weather/city/?city=Томск`

Integration with Yandex is located in _apps/weather/utils/integration.py_