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
    path('admin', views.admin),
    path('admin_login', views.admin_login),
    path('admin_dashboard', views.admin_dashboard),
    path('book', views.book),
    path('new_book', views.new_book),
    path('create_book', views.create_book),
    path('edit/<int:book_id>', views.edit),
    path('update/<int:book_id>', views.update),
    path('delete/<int:book_id>', views.delete)
]
