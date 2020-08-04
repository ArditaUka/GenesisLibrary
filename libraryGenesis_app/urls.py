from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('display_login', views.display_login),
    path('display_register', views.display_register),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('about', views.about),
    # path('books', views.books_list),
]
