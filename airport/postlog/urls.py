from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.FlightListPageView.as_view(), name='flight_list'),
    path('<int:pk>/delete', views.FlightDeletePageView.as_view(), name='flight_delete'),
    path('search/', views.FlightSearchPageView, name='flight_search'),
    path('add/', views.FlightAddPageView, name='flight_add'),
]