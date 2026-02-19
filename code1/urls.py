from django.urls import path 
from code1 import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('service/', views.service, name='service'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'), 
    path('account/', views.account, name='account'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.settings_view, name='settings'),
    path('change-password/', views.change_password, name='change_password'),

]


