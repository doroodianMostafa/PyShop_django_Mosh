from django.urls import path
from . import views


urlpatterns = [
    path('', views.index), # we should not call the function ... we just make a refrence to it
    path('new', views.new)

]