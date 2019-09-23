from django.urls import path

from . import views

app_name='myapp'
urlpatterns = [
    path('', views.home, name='home_page'),
    path('new_search', views.new_search,name='new_search') 
]