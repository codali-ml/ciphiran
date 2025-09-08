from django.urls import path
from . import views

urlpatterns =[
  path('',views.products,name='products'),
  path('<uuid:pk>',views.product,name='product'),

]