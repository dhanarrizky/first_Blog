from typing import Any, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404

from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm  #<-- this use to declaration forms for users members
from django.urls import reverse_lazy
from .forms import SignUpForm, EditUserProfile, PasswordChangeingForm, CreateProfileView
from django.contrib.auth.views import PasswordChangeView

# create a profile views
from django.views.generic import DetailView, CreateView
from artikelBlog.models import Profile #<-- get models from file artikelBlog

class CreateProfileView(CreateView):
    model = Profile
    form_class = CreateProfileView
    template_name = "Registration/create_profile.html"
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShowProfileDetailView(DetailView):
    model = Profile
    template_name = 'Registration/profile_detial.html'
    
    def get_context_data(self, *args,**kwargs):
        #cat_menu = Profile.objects.all()
        context = super(ShowProfileDetailView, self).get_context_data(*args,**kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        context["page_user"] = page_user
        return context
    
class EditProfileDetailView(generic.UpdateView):
    model = Profile
    template_name = 'Registration/profile_edit.html'
    fields = ['bio','profile_pic','instagram_url','hilokal_url','facebook_url','website_url']
    success_url = reverse_lazy('homePage')
    
    

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'Registration/register.html' # <-- if using tempalates registration, we must to use file name is Resgistration
    success_url = reverse_lazy('login')
    
class UserEditProfileView(generic.UpdateView):
    form_class = EditUserProfile
    template_name = 'Registration/edit_profile.html'
    success_url = reverse_lazy('homePage')
    
    def get_object(self):
        return self.request.user #<-- to get the previous value of this page
    
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeingForm
    #form_class = passwordChangeForm
    success_url = reverse_lazy('change-success')
    
    
def change_success(request):
    return render(request, 'Registration/success.html', {})
