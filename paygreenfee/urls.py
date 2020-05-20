from django.urls import path
from . import views


urlpatterns = [
    path('', views.paygreenfee, name='paygreenfee'),
    path('remove/<course_id>/', views.remove_tee_time_from_bag, name='remove_tee_time_from_bag')
]
