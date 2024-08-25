from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('login/', login),
    path('signup/', signup),
    path('logout/', logout),
    path('product/<int:id>', productView),
    path('category/<str:cat>', category),
    path('about/', about),
    path('purchase/<int:prod>', purchase),
]