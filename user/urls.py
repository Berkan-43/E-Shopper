from django.urls import path
from user.views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('update/', user_update, name='user_update'),
    path('password/', change_password, name='change_password'),
    path('login/', auth_views.LoginView.as_view( # LoginView'i kullandığında settings dosyasında LOGIN_REDIRECT_URL = '/' bunu eklemeyi unutma
        template_name = 'login.html'
    ), name='login')
]