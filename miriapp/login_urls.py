from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='miriapp/login.html'),name='login' ),
    path('register/',views.UserFormView.as_view() , name='user-register' ),
    path('logout/',views.UserLogOut.logout_view,name='logout' ),

]
