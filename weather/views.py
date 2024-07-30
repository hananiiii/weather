from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']  # name="city" from the input in index
        try:
            res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=91fc1df85fd6f6757bc247c5ea60c1bc').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp']) + 'K',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }
        except Exception as e:
            data = {"error": str(e)}
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
