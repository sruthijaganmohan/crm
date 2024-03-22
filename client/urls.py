from django.urls import path
from . import views

urlpatterns = [
    path('clients-list/', views.clients_list, name='clients_list'),
    path('view-client/<int:pk>', views.view_client, name='view_client'),
    path('add-client/', views.add_client, name='add_client'),
    path('delete-client/<int:pk>', views.delete_client, name='delete_client'),
    path('update-client/<int:pk>', views.update_client, name='update_client'),
]