from django.urls import path

from . import views
# from views import journeyplan

urlpatterns = [
    path('', views.journeyplan, name='journeyplan'),
]