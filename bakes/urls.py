from . import views
from django.urls import path


urlpatterns = [
    path('', views.BakeList.as_view(), name='home')
]