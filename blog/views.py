from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article

# Create your views here.

class ArticleList(ListView):
	model = Article
	template_name = 'blog/article/article_list.html'
	paginate_by = 4