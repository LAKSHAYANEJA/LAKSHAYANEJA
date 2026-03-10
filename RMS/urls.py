from django.contrib import admin
from django.urls import path
from RMS import views
urlpatterns = [
    path('', views.loginuser, name='loginuser'),
    path('home/', views.index, name='home'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('add_subjects/',views.add_subjects, name='add_subjects'),
    path('view_subjects_list/',views.view_subjects_list,name='view_subjects_list'),
    path('delete/<int:id>', views.delete, name="delete"),               # URL TO GET ID FROM SOME ANOTHER PAGE
    path('update/<int:id>', views.update, name="update"),    
    path('assign_subjects/', views.assign_subjects, name="assign_subjects"),   
    path('view_assigned_subjects_list/', views.view_assigned_subjects_list, name="view_assigned_subjects_list"), 
    path('delete_assigned_subjects/<int:id>', views.delete_assigned_subjects, name="delete_assigned_subjects"), 
    path('update_assigned_subjects/<int:id>', views.update_assigned_subjects, name="update_assigned_subjects"), 
    path('add_students/', views.add_students, name="add_students"),
    path('assign_roll_number_to_students/', views.assign_roll_number_to_students, name="assign_roll_number_to_students"),   

]
