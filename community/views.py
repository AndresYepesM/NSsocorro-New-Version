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
# Create your views here.


# Members of the Community. 

class MembersList(ListView):
	model = MembersProfile
	template_name = 'community/Members/members_list.html'
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