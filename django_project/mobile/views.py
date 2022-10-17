from django.shortcuts import render
from django.http import HttpResponse
# Register your models here.
from .models import Mobile
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

mobile_details=[{
    'brand': 'Apple',
    'model': 'iPhone SE',
    'base_color': 'Black',
    'processor': 'water',
    'screen_size': 'Very Small',
    'ROM': '64',
    'RAM': '2',
    'display_size': '4.7',
    'num_rear_camera': '1',
    'num_front_camera': '1',
    'battery_capacity': '1800',
    'ratings': '4.5',
    'num_of_ratings': ' 38645',
    'sales_price': '32999',
    'discount_percent': '0.17',
    'sales': '127.52',
    'units_sold': '38643', 
},
{
    'brand': 'Apple',
    'model': 'iPhone 12 Mini',
    'base_color': 'Red',
    'processor': 'Ceramic',
    'screen_size': 'Small',
    'ROM': '64',
    'RAM': '4',
    'display_size': '5.4',
    'num_rear_camera': '2',
    'num_front_camera': '1',
    'battery_capacity': '2815',
    'ratings': '4.5',
    'num_of_ratings': '244',
    'sales_price': '57149',
    'discount_percent': '0.04',
    'sales': '1.39',
    'units_sold': '243', 
}

]


def home(request):
    context={
        'mobile_details':Mobile.objects.all()                        # 'mobile_details':mobile_details
    }
    return render(request,'mobile/home.html',context)
    # return HttpResponse('<h1>Mobile Home</h1>')



class MobileListView(ListView):
    model=Mobile
    template_name='mobile/home.html'            #<app>/<model>_<viewtype>.html
    context_object_name='mobile_details'
    ordering=['units_sold']                     #with - in front it can be desc



class MobileDetailView(DetailView):
    model=Mobile


class MobileCreateView(CreateView):
    model=Mobile
    fields=['brand','model']
    
    

def about(request):
    return render(request,'mobile/about.html',{'title':'About'})
    # return HttpResponse('<h1>Mobile About</h1>')
