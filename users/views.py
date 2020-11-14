from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .form import UserRegisterForm,UserUpdateFrom,ProfileUpdateFrom
from django.contrib.auth.mixins import LoginRequiredMixin



class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form  = UserRegisterForm()
        return render(request, 'users/register.html', {'form':form})
        
    def post(self, request, *args, **kwargs):
        form  = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            form.save()
            messages.success(request,f"Account creted for {username}")
            return redirect('login')
        return render(request, 'users/register.html', {'form':form})

class ProfileView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        u_form = UserUpdateFrom(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)
        return render(request, 'users/profile.html', {'u_form':u_form,'p_form':p_form})
        
    def post(self, request, *args, **kwargs):
        u_form = UserUpdateFrom(request.POST,instance=request.user)
        p_form = ProfileUpdateFrom(request.POST, request.FILES ,instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request,f"Account has been updated !!")
            return redirect('profile')
        return render(request, 'users/profile.html', {'u_form':u_form,'p_form':p_form})
