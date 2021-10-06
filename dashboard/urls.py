from dashboard import views
from django.urls import path
from django.contrib.auth import views as auth_views

from dashboard.forms import LoginForm
urlpatterns = [
    path("", views.home, name = "home"),
    path("notes/",views.notes, name = "notes"),
    path("delete_note/<int:pk>/", views.delete_note, name = "delete_note"),
    path("notes_detail/<int:pk>/", views.notes_detail, name = "notes_detail"),
    path("homework/", views.homework, name = "homework"),
    path("update_homework/<int:pk>/", views.update_homework, name = "update_homework"),
    path("delete_homework/<int:pk>/", views.delete_homework, name = "delete_homework"),
    #path("youtube/", views.youtube, name = "youtube"),
    path("todo/", views.todo, name = "todo"),
    path("update_todo/<int:pk>/", views.update_todo, name = "update_todo"),
    path("delete_todo/<int:pk>/", views.delete_todo, name = "delete_todo"),
    path("books/", views.books, name = "books"),
    path("dictionary/", views.dictionary , name = "dictionary"),
    path("wiki/", views.wiki, name = "wiki"),
    path("youtube/", views.youtube, name = "youtube"),
    path("conversion/", views.conversion, name = "conversion"),
    path("register/", views.register, name = "register"),
    path("accounts/login/", auth_views.LoginView.as_view(template_name = "dashboard/login.html", authentication_form = LoginForm),name = "login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "dashboard/logout.html",),name = "logout"),



]