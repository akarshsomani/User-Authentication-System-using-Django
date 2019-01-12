from django.urls import path
from . import views
urlpatterns = [
   path('authenticate/', views.home, name='home'),#for calling the home function in the views.py folder
   #use this 'home' for providing in links in the html.
   path('authenticate/login/', views.login_user, name='login'),
   path('authenticate/logout/', views.logout_user, name='logout'),
   
   path('authenticate/register/', views.register_user, name='register'),
   path('authenticate/edit_profile/', views.edit_profile, name='edit_profile'),
   path('authenticate/change_password/', views.change_password, name='change_password'),


]
