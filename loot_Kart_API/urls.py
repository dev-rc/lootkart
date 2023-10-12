

from django.urls import path
from .views import ProductAPIView
app_name = 'api'

urlpatterns = [
    path('', ProductAPIView.as_view(), name='api'),
]
