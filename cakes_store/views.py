from re import template
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from cakes_store.forms import UserCreationForm


def index(request):
    context = {
        'Step': 'Number',
    }
    return render(request, 'index.html', context)


class Signup(View):

    template_name = 'signup.html'

    def get(self, request):
        context ={
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
