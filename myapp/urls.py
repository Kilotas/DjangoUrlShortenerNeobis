from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go'),
    path('url/<str:uuid>', views.redirect_long_url),
    path('url/stats/<str:uuid>', views.get_long_url),
]

