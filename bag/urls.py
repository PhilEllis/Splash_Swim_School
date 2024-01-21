from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/', views.add_course_to_bag, name='add_course_to_bag'),
    path(
        'remove/<course_id>/',
        views.remove_course_from_bag,
        name='remove_course_from_bag'
    ),
]
