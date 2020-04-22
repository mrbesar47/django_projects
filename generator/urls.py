from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.generator, name='generator'),
    path('generatedpassword/', views.generatedpassword, name='password'),

]