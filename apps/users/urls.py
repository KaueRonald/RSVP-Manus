from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=LoginForm, redirect_authenticated_user=True, ), name='login'),
    # path('login/',  auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True,), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout',),

    # path('register/', views.RegisterView.as_view(),                     name='register'),
]
