from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
		path('',views.baggageListPageView.as_view(), name ='baggage_list'),
		path('add/',views.baggageAddPageView.as_view(), name = 'baggage_add'),
		path('<int:pk>/delete/', views.baggageDeletePageView.as_view(), name='baggage_delete'),
		path('update/<int:pk>/', views.baggageUpdatePageView.as_view(), name='baggage_update'),
		path('search/', views.baggageSearch, name='baggage_search'),
		path('add/ajax/load-flight/', views.load_flight, name='ajax_load_flight'),
		path('add/ajax/load-name/', views.load_name, name='ajax_load_name')
		#add another url for load_name
]
