from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page),
    path('home/', views.home_page),
    path('aboutus/', views.about_us_page),
    path('clients/<clientid>', views.client_info)
]