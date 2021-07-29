from django.contrib import admin
from django.urls import path
from trabajofinal.views import inicio


urlpatterns = [
    path('', inicio),

]