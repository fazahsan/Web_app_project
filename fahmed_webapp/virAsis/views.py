from django.shortcuts import get_object_or_404, render,redirect
import requests
from .models import ElecDom
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm    

def home(request):
    appliances = ElecDom.objects.all()
   
    return render(request, 'virAsis/home.html', {'appliances': appliances})

def control_appliance(request, appliance_id):
    appliance = get_object_or_404(ElecDom, id=appliance_id)
    if request.method == 'POST':
        appliance.status = not appliance.status
        appliance.save()
        return redirect('home')
    return render('home')
def main(request):
    return render(request,'virAsis/main.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(
                subject,
                f"Message from {name} ({email}):\n\n{message}",
                email,
                ['recipient@example.com'],
                )

                if  messages.success(request, 'Your message has been sent successfully.'):
                    return redirect('contact')
            except Exception as e:  
                messages.error(request, 'There was an error sending your message. Please try again later.')
                print(f"Error sending email: {e}")
                return redirect('home')
    else:
        form = ContactForm()
        return render(request, 'virAsis/contact.html', {'form': form})
def fetch_thinger_data(request):
    api_url = 'https://backend.thinger.io/v3/users/ahsan/devices/smarthome/resources/dht11'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkZXZpY2UiLCJzdnIiOiJldS1jZW50cmFsLmF3cy50aGluZ2VyLmlvIiwidXNyIjoiYWhzYW4ifQ.TsH5AsgK-esBzwvSfz9zifXB3kdhDRgrfVHANptVVhw'
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()  # Parse the JSON data
        print(data)
        if (data['celsius']==None) or (not data):
            data={'temperature':30,'humidity':'60%'}

    except requests.exceptions.HTTPError as http_err:
        data = {'error': str(http_err)}
        data =  data={'temperature':30,'humidity':'60%'}
    except Exception as err:
        #data = {'error': str(err)}
        data =  data={'temperature':30,'humidity':'60%'}

    return render(request, 'virAsis/thinger_data.html', {'data': data})