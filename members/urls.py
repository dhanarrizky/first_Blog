from django.urls import path

from .views import UserRegisterView,UserEditProfileView,ChangePasswordView,CreateProfileView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register-page'),
    #path('login/',UserRegisterView.as_view(),name='login'),
    path('edit_profile/',UserEditProfileView.as_view(), name='edit_profile'),
    #makae change password page
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='Registration/change_password.html')),
    path('password/',ChangePasswordView.as_view(template_name='Registration/change_password.html')),
    path('change_success/', views.change_success, name='change-success'),
    
    path('<int:pk>/profile/',views.ShowProfileDetailView.as_view(), name='profile-detile-page'),
    path('<int:pk>/edit_profile/',views.EditProfileDetailView.as_view(), name='profile-edit-page'),
    path('create_profile/', CreateProfileView.as_view(), name='create-profile'),
    
]
