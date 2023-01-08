from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('upload/',  Upload.as_view(), name='upload')

]