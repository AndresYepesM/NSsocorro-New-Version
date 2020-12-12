from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MembersProfile

# Create your views here.


# Members of the Community. 

class MembersProfile(ListView):
	model = MembersProfile
	template_name = 'community/Members/members_list.html'
	paginate_by = 9