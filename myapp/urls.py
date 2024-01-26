from django.urls import path
from . import views
urlpatterns = [
    path('url/<str:uuid>', views.redirect_long_url),
    path('url/', views.url_shorten_api_view),
    path('url/stats/<str:uuid>', views.get_long_url),

]