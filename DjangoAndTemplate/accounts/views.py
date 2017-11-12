from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
)
from django.contrib.auth import login
from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        login(self.request, self.object)
        return reverse('home')
