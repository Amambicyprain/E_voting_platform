from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from django.views.generic import ListView
from campay.sdk import Client
from polls.models import *
# Create your views here.

def home_page(request):
	candidates = Choice.objects.all().order_by('-vote')
	print(candidates)
	top_four_candidates = candidates[:4]
	context ={
		'top_four_candidates':top_four_candidates,
	}
	return render(request,'polls/index.html',context=context)

# class Candidates_page(ListView):
# 		model=Choice
# 		paginate_by= 6
# 		def get_queryset(self):
# 			return Choice.objects.all().order_by('candidate_number')

		

def candidates_page(request):
	candidates = Choice.objects.all()
	# paginator = Paginator(candidates, 3)
	# page_number = request.GET.get('page')
	# candidates = paginator.get_page(page_number)
	# choice_list = Choice.objects.all()

	# pagination
	paginator = Paginator(candidates, 6) # Show 25 contacts per page.
	page_number = request.GET.get('page')
	candidates = paginator.get_page(page_number)

	context = {
	'candidates':candidates,
	
	}
	return render(request,'polls/choice_list.html',context = context)

def statistics(request):
	candidates = Choice.objects.all().order_by('-vote')
	context = {
	'candidates':candidates,
	}
	return render(request,'polls/detail.html', context=context)
	


def payment_page(request, candidate_id):
	get_candidate = Choice.objects.get(id = candidate_id)

	return render(request,'polls/payment_form.html', {'get_candidate':get_candidate})
		


def candidate_profile(request, candidates_id):
	candidate = get_object_or_404(Choice,pk = candidates_id)
	print('id: ',candidates_id)
	context = {'candidate':candidate}
	return render(request,'polls/profile.html',context=context)





def Register_Candidate(request):
	form = RegisterCandidateForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			candidates = form.save()
			return redirect('/')
		print(request.method)
	context = {
	'form':form

	}
	return render(request, 'polls/candidate_form.html',context = context)


def add_candidate(request):
	user = request.user
	if request.POST:
		print(request.POST)
		candidate = Choice()
		candidate.candidate_number = request.POST['candidate_number']
		candidate.candidate_name   = request.POST['candidate_name']
		candidate.candidate_status   = request.POST['candidate_status']
		candidate.candidate_email   = request.POST['candidate_email']
		candidate.candidate_tel   = request.POST['candidate_tel']
		candidate.candidate_date_birth   = request.POST['candidate_date_birth']
		candidate.candidate_carrier_history   = request.POST['candidate_carrier_history']
		if 'candidate_image' in request.FILES:
			candidate.candidate_image  = request.FILES['candidate_image']
		candidate.candidate_role   = request.POST['candidate_role']
		candidate.save()

		return redirect('candidates_page')
	else:
		return render(request, 'polls/candidate_form.html', {})


def search_candidate(request):
	urser = request.user
	if request.POST:
		print(request.POST)
		searched_name = request.POST['searched_word']
		print(searched_name)
		candidate_gotten = Choice.objects.filter(candidate_name__contains = searched_name)
		print(candidate_gotten)

		context ={
		 'candidate_gotten': candidate_gotten
		}
		return render (request, 'polls/search_result.html',context = context)
	else:
		return  render (request, 'polls/search_result.html',{})

def delete_candidate(request,candidate_id):
	candidate = Choice.objects.get(id =candidate_id)
	candidate.delete()
	print(request.method)
	return redirect('candidates_page')
	
def update_candidate(request,candidate_id):
	candidate = Choice.objects.get(id=candidate_id )
	if request.POST:
		print(request.POST)
		
		candidate.candidate_number = request.POST['candidate_number']
		candidate.candidate_name   = request.POST['candidate_name']
		candidate.candidate_status   = request.POST['candidate_status']
		candidate.candidate_email   = request.POST['candidate_email']
		candidate.candidate_tel   = request.POST['candidate_tel']
		candidate.candidate_date_birth   = request.POST['candidate_date_birth']
		candidate.candidate_carrier_history   = request.POST['candidate_carrier_history']
		
		if 'candidate_image' in request.FILES:
			candidate.candidate_image  = request.FILES['candidate_image']
		candidate.candidate_role   = request.POST['candidate_role']
		candidate.save()
		return redirect('candidates_page')
	return render(request, 'polls/candidate_form_edit.html', { 'candidate':candidate})


############## campay #############################
campay = Client({
    "app_username" : "UPsdL44n9oLAFYvd0bo-D-Lqf3YATVPysl8xBRIIj23Gu4XkXj0NfW77sUOe4tWFJ2GGSZKHgUSphVJjvLRapg",
    "app_password" : "ZxX8_JlxxSjKqkUvM3Id9Vq78xu8KHhtl7wfWeljoMran1EChrOYkZWGs_LY30-9E71ZdLbAakWIRe7-a9fYhA",
    "environment" : "DEV" #use "DEV" for demo mode or "PROD" for live mode
})
def collect_payment(request):
	user = request.user
	if request.POST:
		get_candidate = Choice.objects.get(id = request.POST['candidate_id'])
		candidate_vote = request.POST['number_votes']
		print(request.POST)
		unit_price = 2
		number = request.POST['phone_number']
		fl_num = '237' + number
		number_votes = int(request.POST['number_votes'])
		bill = number_votes * int(unit_price)
		print(fl_num)
		print(bill)

		collect = campay.collect({
         "amount": bill, #The amount you want to collect
         "currency": "XAF",
         "from": fl_num, #Phone number to request amount from. Must include country code
         "description": "testing sdk"
      })

		trans_status = collect.get("status")
		if trans_status == 'SUCCESSFUL':
			get_candidate.vote += number_votes
			get_candidate.save()	
			print("############")
			print(trans_status)
			print("############")
		if trans_status == 'FAILED':
		    print("Transaction failed for unknown reasons")
		if trans_status == 'SUCCESSFUL':
		    print("Transaction SUCCESSFUL")

		print("Done!!")
		
		return redirect('/')
