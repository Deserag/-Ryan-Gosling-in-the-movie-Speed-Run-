
from django.contrib import admin
from django.urls import path, re_path
import games.views
import account.views



urlpatterns = [
    path('', games.views.osnos),
    re_path(r'^Game_', account.views.accounts)
]
