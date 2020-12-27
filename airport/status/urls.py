from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.StatusListPageView.as_view(), name='status_list'),
    path('<int:pk>/delete/', views.StatusDeletePageView.as_view(), name='status_delete'),
	path('search/', views.SearchKey, name='status_search'),
	path('update/<int:pk>/', views.StatusUpdatePageView.as_view(), name='status_update'),    
	path('add/', views.StatusAddPageView.as_view(), name='status_add'),
	path('add/ajax/load-park/', views.load_park_bay, name='ajax_load_park'),
    path('add/ajax/load-dest/', views.load_destination, name='ajax_load_dest'),
    path('add/ajax/load-dept/', views.load_departure, name='ajax_load_dept'),
]