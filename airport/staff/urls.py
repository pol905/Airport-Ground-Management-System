from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('',views.CrewListPageView.as_view(), name ='crew_list'),
	path('add/',views.CrewAddPageView.as_view(), name = 'crew_add'),
	path('<int:pk>/delete/', views.CrewDeletePageView.as_view(), name='crew_delete'),
	path('update/<int:pk>/', views.CrewUpdatePageView.as_view(), name='crew_update'),
	path('search/', views.CrewSearch, name='crew_search')

]
