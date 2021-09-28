from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('password/', views.change_password, name='change_password'),
    path('change-profile-image/', views.add_pro_pic, name='add_pro_pic'),
    path('change-profile-pic/', views.change_pro_pic, name='change_pro_pic'),
]
