# apis/urls.py
from django.urls import path
from .views import DataView

urlpatterns = [

    path('check-data/', DataView.as_view())
    
]
