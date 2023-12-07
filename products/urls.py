from django.urls import path
from . import views

urlpatterns = [
    path('level1/', views.level1_courses, name='level1_courses'),
    path('level2/', views.level2_courses, name='level2_courses'),
    path('level3/', views.level3_courses, name='level3_courses'),
    path('level4/', views.level4_courses, name='level4_courses'),
]
