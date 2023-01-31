from . import views
from django.urls import path


urlpatterns = [
    path('', views.BakeList.as_view(), name='home'),
    path('mystarredbakes/', views.MyStarredBakes.as_view(), name='my-starred-bakes'),
    path('bestforbakes/', views.BestForBakes.as_view(), name='best-for-bakes'),
    path('star/<slug:slug>', views.BakeStar.as_view(), name='bake-star'),
    path('bake-detail/<slug:slug>/', views.BakeDetail.as_view(), name='bake-detail'),
    path('add-bake/', views.AddBake.as_view(), name='add-bake'),
    path('edit-bake/<slug:slug>/', views.UpdateBake.as_view(), name='edit-bake'),
    path('delete-bake/<slug:slug>/', views.DeleteBake.as_view(), name='delete-bake'),
]