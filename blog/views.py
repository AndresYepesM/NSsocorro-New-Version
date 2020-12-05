from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article, Activity
from .forms import NewArticle, NewActivities

# Create your views here.


########################################### Article's Views ################################################################

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


@login_required(login_url='/login')
def ArticleDelete(request, pk):

	post = get_object_or_404(Article, id=pk)
	post.delete()
	return redirect('article')

########################################### Activity's Views ################################################################

class ActivitiesList(ListView):
	model = Activity
	template_name = 'blog/activities/activities_list.html'
	paginate_by = 4


@login_required(login_url='/login')
# Msj the artiicle created with success.
def msj_activities(request):
	return render(request, 'blog/activities/msj_activities.html')


class ActivitiesCreate(CreateView):
	model = Activity
	form_class = NewActivities
	template_name = 'blog/activities/activities_form.html'
	success_url = reverse_lazy('msj_activities')

class ActivitiesUpdate(UpdateView):
	model = Activity
	form_class = NewActivities
	template_name = 'blog/activities/activities_form_upgrade.html'
	success_url = reverse_lazy('msj_activities')

@login_required(login_url='/login')
def ActivitiesDelete(request, pk):

	post = get_object_or_404(Activity, id=pk)
	post.delete()
	return redirect('activities')
