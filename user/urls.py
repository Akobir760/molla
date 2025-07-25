from django.urls import path
from user.views import register_page_view 


app_name = 'register'

urlpatterns = [
    path('register', register_page_view, name='home'),
]