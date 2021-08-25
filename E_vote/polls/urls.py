
from django.urls import path
from polls import views
from . views import *

urlpatterns = [
	path('',views.home_page, name = 'home_page'),

	path('candidates/',views.candidates_page, name = 'candidates_page'),

	path('candidates/register/',views.add_candidate, name = 'Register_Candidate'),

	path('candidates/candidate_profile/<int:candidates_id>/',views.candidate_profile, name = 'candidate_profile'), 

	path('statistics',views.statistics,name= 'statistics'),

	path('candidates', add_candidate, name= 'add_candidate'),

	path('payment', collect_payment, name= 'collect_payment'),

	path('payment_page/<candidate_id>/', payment_page, name='payment_page'),

	path('candidates/search/', search_candidate, name='search_candidate'),
	path('candidates/delete/<candidate_id>/', delete_candidate, name='delete_candidate'),

]

