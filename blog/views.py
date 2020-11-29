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
from .forms import ArticleCreate

# Create your views here.

@login_required(login_url='/login')
# Msj the artiicle created with success.
def msj_article(request):
	return render(request, 'blog/article/msj_article.html')

class ArticleList(ListView):
	model = Article
	template_name = 'blog/article/article_list.html'
	paginate_by = 4

class ArticleCreate(CreateView):
	model = Article
	form_class = ArticleCreate
	template_name = 'blog/article/article_form.html'
	success_url = reverse_lazy('msj_article')