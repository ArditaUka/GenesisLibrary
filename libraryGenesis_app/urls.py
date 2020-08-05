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
    path('book', views.book),
    path('new_book', views.new_book),
    path('create_book', views.create_book),
    path('edit/<int:book_id>', views.edit),
    path('update/<int:book_id>', views.update),
    path('delete/<int:book_id>', views.delete),
    path('display_genre/<str:genre>', views.display_genre),
    path('display/<int:book_id>', views.display),
    path('borrow_info/<int:book_id>', views.borrow_info),
    path('borrow/<int:book_id>', views.borrow),
    path('borrow_book/<int:book_id>', views.borrow_book),
    path('display_borrowed', views.display_borrowed),
    path('return_book/<int:book_id>', views.return_book),

]
