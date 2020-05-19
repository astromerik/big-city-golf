from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('book/', views.book_course, name='book_course'),
]
