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
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from .forms import RegistroForm, ProfileUpdate

# Create your views here.


# Admin Home Page

@login_required(login_url='/login')
# Admin Page 
def admin_home(request):
	return render(request, 'administration/admin_home.html')



@login_required(login_url='/login/')
# msj cretae user success
def msj_success(request):
	return render(request, 'registration/new_user_success.html')


@login_required(login_url='/login/')
# msj update user profile success
def profile_success(request):
	return render(request, 'administration/profile_success.html')



@login_required(login_url='/login/')
# sing up view
def signup(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('new_user')
	else:
		form = RegistroForm()
	return render(request, 'registration/singup.html', {
		'form': form
		})


# Update profile view
class UserEditView(generic.UpdateView):
	form_class = ProfileUpdate
	template_name = 'administration/profile_edit.html'
	success_url = reverse_lazy('profile_update')

	def get_object(self):
		return self.request.user