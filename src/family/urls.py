from django.urls import path
from family import views

urlpatterns = [
    path('', views.index)
]
