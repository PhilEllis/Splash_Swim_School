from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
    ),
    path('delete_guardian/', views.delete_guardian, name='delete_guardian'),
    path(
        'update-child/<int:child_id>/',
        views.update_child_profile,
        name='update_child_profile'
    ),
    path(
        'delete-child/<int:child_id>/',
        views.delete_child_profile,
        name='delete_child_profile'
    ),
]
