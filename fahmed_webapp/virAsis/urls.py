from django.urls import path
from  .views import control_appliance, home,main,contact_view,fetch_thinger_data
urlpatterns = [
    
    path('', main, name='main'),
    path('home/', home, name='home'),
    path('contact/', contact_view, name='contact'),
     path('thinger/', fetch_thinger_data, name='thinger'),
    path('control/<int:appliance_id>/', control_appliance, name='control_appliance'),
    
]