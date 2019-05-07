from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    # url(r'^register', views.registration, name='registration'),
    url(r'status', views.status, name='status'),
    path('addUser', views.addUser, name='addUser'),
    path('getUser', views.getUser, name='getUser'),
    # path('showInfo', views.indexForLogged, name='index2'),
    url(r'^$', views.index, name='index'),
    
]
