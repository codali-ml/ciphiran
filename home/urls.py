from django.urls import path
from . import views

urlpatterns =[
  path('',views.home,name='home'),
  path('contact-us/',views.contact,name='contact'),
  path('about-us/',views.aboutUs,name='aboutUs'),
  path('careers/',views.career,name='careers'),

]