from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
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

class Candidates_page(ListView):
		model=Choice
		paginate_by= 6
		def get_queryset(self):
			return Choice.objects.all().order_by('candidate_number')

		

def candidates_page(request):
	candidates = Choice.objects.all()
	paginator = Paginator(candidates, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context = {
	'candidates':candidates,
	'page_obj':page_obj
	
	}
	return render(request,'polls/choice_list.html',context = context)

def statistics(request):
	candidates = Choice.objects.all().order_by('-vote')
	context = {
	'candidates':candidates,
	}
	return render(request,'polls/detail.html', context=context)
	


def payment_page(request):

	return render(request,'polls/payment_form.html')
	


def vote(request,candidates_id):
	candidate = get_object_or_404(Choice,pk = candidates_id)
	candidate.vote +=1
	candidate.save()
	return render(request,'polls/payment_form.html')
	