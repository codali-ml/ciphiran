from django.urls import path
from . import views

urlpatterns =[
  path('',views.services,name='services'),
  path('<uuid:pk>',views.service,name='service'),
 
]