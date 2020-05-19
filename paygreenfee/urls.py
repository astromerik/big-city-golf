from django.urls import path
from . import views


urlpatterns = [
    path('', views.paygreenfee, name='paygreenfee'),
    path('delete_tee_time/<int:tee_time_id>/',
         views.delete_tee_time, name='delete_tee_time'),
    # path('cache_checkout_data/',
    #      views.cache_checkout_data, name='cache_checkout_data')
]
