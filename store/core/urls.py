from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .forms import LoginForm


app_name = 'core'
urlpatterns = [
path ('', views.index, name='index'),
path ('contact/', views.contact, name='contact'), 
#path('about/', views.about, name='about'),
path('signup/', views.signup, name='signup'),
path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
path('profile/', views.profile, name='profile'),
#path('accounts/', include('core.urls')),
#path('edit_profile/', views.edit_profile, name='edit_profile'),
]