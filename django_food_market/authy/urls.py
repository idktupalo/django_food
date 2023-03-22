from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registry/', views.registry, name='registry'),
    path('logout/', views.logout, name='logout')
]