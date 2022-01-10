from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MembersProfile
from .forms import *
# Create your views here.


# Members of the Community. 

class MembersList(ListView):
	model = MembersProfile
	template_name = 'community/Members/members_list.html'
	paginate_by = 9


class NewMember(CreateView):
	model = MembersProfile
	form_class = CreateMember
	template_name = 'community/Members/members_form.html'
	success_url = reverse_lazy('MembersDone')

class UpdateMember(UpdateView):
	model = MembersProfile
	form_class = CreateMember
	template_name = 'community/Members/members_form.html'
	success_url = reverse_lazy('MembersDone')

@login_required(login_url='/login')
def MemberDelete(request, pk):

	post = get_object_or_404(MembersProfile, id=pk)
	post.delete()
	return redirect('MembersDeleteDone')

class MembersDone(ListView):
	model = MembersProfile
	template_name = 'community/Members/members_done.html'
	paginate_by = 9

class MembersDeleteDone(ListView):
	model = MembersProfile
	template_name = 'community/Members/members_delete_done.html'
	paginate_by = 9

	

@login_required(login_url='/login/')
# Search bar
def SearchMenmers(request):
	return render(request, 'community/Members/members_search.html')


@login_required(login_url='/login/')
# Search Form

def SearchForm(request):

	if request.method == 'POST':

		searched = request.POST['searched']
		members = MembersProfile.objects.filter(name__contains=searched)
		return render(request, 'community/Members/members_search_result.html', {'searched':searched, 'members':members})

	else:

		return render(request, 'community/Members/members_list.html')