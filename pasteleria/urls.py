from django.urls import path

from . import views
app_name = 'pasteleria'
urlpatterns = [
    path('', views.index, name='index'),
]