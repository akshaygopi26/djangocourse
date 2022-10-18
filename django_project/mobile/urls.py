from django.urls import path
from . import views 
from  .views import (
    MobileListView,
    MobileDetailView,
    MobileCreateView,
    BrandMobileListView
)


urlpatterns = [
    path('',MobileListView.as_view(),name='mobile-home'),
    path('brand/<str:brand>',BrandMobileListView.as_view(),name='mobile-brand'),
    path('mobile/<int:pk>',MobileDetailView.as_view(),name='mobile-detail'),                      # path('', views.home,name='mobile-home'),  MobileListView.as_view()
    path('mobile/new/',MobileCreateView.as_view(),name='mobile-create'),
    path('about/', views.about,name='mobile-about')
]





#so line numbr 7 will look for  <app>/<model>_<viewtype>.html  ie mobile/mobile_list.html