from django.urls import path

from . import views
# from views import routes

urlpatterns = [
    path('', views.routes, name='routes'),
]