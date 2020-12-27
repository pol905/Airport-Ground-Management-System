from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
		path('',views.passengerListPageView.as_view(), name ='passenger_list'),
		path('add/',views.passengerAdd, name = 'passenger_add'),
		path('<int:pk>/delete/', views.passengerDeletePageView.as_view(), name='passenger_delete'),
		path('update/<int:pk>/', views.passengerUpdatePageView.as_view(), name='passenger_update'),
		path('search/', views.passengerSearch, name='passenger_search')

]
