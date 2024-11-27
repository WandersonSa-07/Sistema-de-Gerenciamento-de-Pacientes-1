from django.urls import path
from core.views.home import home_view

urlpatterns = [
    path("", home_view, name='home')
]