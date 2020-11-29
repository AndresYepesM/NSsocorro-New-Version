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
from .forms import NewArticle

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
	form_class = NewArticle
	template_name = 'blog/article/article_form.html'
	success_url = reverse_lazy('msj_article')

class ArticleUpdate(UpdateView):
	model=Article
	form_class=NewArticle
	template_name='blog/article/article_form_update.html'
	success_url=reverse_lazy('msj_article')

#class ArticleDelete(DeleteView):
#	model=Article
#	template_name='blog/article/article_list.html'
#	success_url=reverse_lazy('article')

@login_required(login_url='/login')
def ArticleDelete(request, pk):

	post = get_object_or_404(Article, id=pk)
	post.delete()
	return redirect('article')