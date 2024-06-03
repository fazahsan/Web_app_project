from django.shortcuts import render,redirect
from .models import ElecDom
import requests
THINGER_URL = "https://backend.thinger.io/v3/users/ahsan/devices/smarthome/resources/dht11"
THINGER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTY0NTY3MjIsImlhdCI6MTcxNjQ0OTUyMiwicm9sZSI6InVzZXIiLCJ1c3IiOiJhaHNhbiJ9.I-7Q5RRMj76m867Yo3jBHDNNJXiz6btX2H_FHJcvmEQ"
def fetchdata():
    response=requests.get(f"{THINGER_URL}data",headers={"Authorization ":f"Bearer{THINGER_TOKEN}"})
    data =response.json()
    if data:
        return data
    else:
        data= {'temperature':30,'humidity':'50%'}
    return data
def control_appliance(request,app_id):
    appliance = ElecDom.objects.get()
    action = request.POST.get("action")
    
    # Toggle status
    appliance.status = not appliance.status
    appliance.save()

    # Send command to Thinger.io
    requests.post(
        f"{THINGER_URL}{appliance.name}",
        headers={"Authorization": f"Bearer {THINGER_TOKEN}"},
        json={"in": appliance.status}
    )
    return redirect('home')

def home(request):
    appliances = ElecDom.objects.all()
    data = fetchdata()
    for appliance in appliances:
        appliance.temperature = data.get('temperature')
        appliance.humidity = data.get('humidity')
        appliance.save()

    return render(request, 'virAsis/home.html', {'appliances': appliances})


