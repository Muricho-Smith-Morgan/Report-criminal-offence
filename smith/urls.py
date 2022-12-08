from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.signup, name='signup'),
    path('login/', views.login.as_view(), name= 'login'),
    path('index/', views.index, name= 'index'),
    path('logout/', views.logout_user.as_view(), name= 'logout'),
]