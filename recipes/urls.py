from recipes.views import home, contato, sobre
from django.urls import path

# Register your models here.
urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]