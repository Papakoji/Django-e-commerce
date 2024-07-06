from django.urls import path 
from . import views 

#URL configs
#You would want to include the url and the function that needs to be called
urlpatterns = [
    path('hello/', views.hello)
]