from . import views
from django.urls import path


urlpatterns = [
    path('', views.BakeList.as_view(), name='home'),
    path('mystarredbakes/', views.MyStarredBakes.as_view(), name='my-starred-bakes'),
    path('star/<slug:slug>', views.BakeStar.as_view(), name='bake-star'),
    path('<slug:slug>/', views.BakeDetail.as_view(), name='bake-detail'),
    
]