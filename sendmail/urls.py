from django.urls import path
from . import views

app_name = 'sendmail'

urlpatterns = [
    path('', views.enter_email, name='enter_email'),
    path('list/', views.list_email, name='list_email'),
]