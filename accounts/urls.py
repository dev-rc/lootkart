

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Add this if you have a login view
    # Add more URLs for other views as needed
]
