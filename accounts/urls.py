from django.urls import path
from django.contrib.auth import views as auth_views
from .views import * 

urlpatterns = [
    path('register/', register_user, name='register'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'), 
    path('change-password/', change_password, name='change-password'), 
    path('update-profile/', update_profile, name='update-profile'),
    path('admin-reset-user-password', admin_reset_user_password, name='admin-reset-user-profile'), 

    # reset password links (default from django)
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name = "accounts/reset_password.html"), name ='reset_password'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"), name ='password_reset_complete'),
]