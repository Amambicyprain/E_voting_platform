from django.urls import path
from polls import views

urlpatterns = [
	path('',views.home_page, name = 'home_page'),
	path('payment/',views.payment_page, name = 'payment_page'),
	path('candidates/',views.Candidates_page.as_view(), name = 'candidates_page'),
	path('vote/<int:candidates_id>/',views.vote, name = 'vote'), 
	path('statistics',views.statistics,name= 'statistics'),
	
]
