from django.urls import path
from . import views

urlpatterns = [
    path('leads-list/', views.leads_list, name='leads_list'),
    path('view-lead/<int:pk>', views.view_lead, name='view_lead'),
    path('add-lead/', views.add_lead, name='add_lead'),
    path('delete-lead/<int:pk>', views.delete_lead, name='delete_lead'),
    path('update-lead/<int:pk>', views.update_lead, name='update_lead'),
]