from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Article, Activity

# Create your views here.

def home(request):
	return render(request, 'readers/home.html')


class Article(ListView):
	model = Article
	template_name = 'readers/article.html'
	paginate_by = 4


class Activities(ListView):
	model = Activity
	template_name = 'readers/activities.html'
	paginate_by = 4