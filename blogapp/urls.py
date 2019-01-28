from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('logon', views.logon, name="login"),
    path('signup', views.signup, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('accounts/login', auth_views.View.as_view(template_name='registration/profile.html')),
]