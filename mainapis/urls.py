from django.urls import path
from . import views

urlpatterns = [
    path('', views.WhatsappApi.as_view(), name='api'),
]
