from django.urls import path
from . import views


urlpatterns = [
    path('', views.golfprofile, name='golfprofile'),
    path('delete_tee_time/<tee_time_id>/', views.delete_tee_time, name='delete_tee_time'),
]