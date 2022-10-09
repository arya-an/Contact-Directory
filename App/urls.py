from django.contrib import admin
from django.urls import path
from App import views
from App.views import *
 

urlpatterns = [
    path('', views.contactlist,name='contactlist'),
    path('newcontact', views.addcontact,name='addcontact'),
    path('detail/<pk>/',ContactDetail.as_view(),name='ContactDetail'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    
]