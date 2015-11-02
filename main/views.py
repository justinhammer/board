from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.views.generic.detail import DetailView

from main.models import CustomUser
from main.forms import CustomUserCreationForm
# Create your views here.


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_detail_view.html'
    slug_field = 'username'


def signup(request):

    context = {}

    form = CustomUserCreationForm()

    context['form'] = form

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            try:
                new_user = CustomUser.objects.create_user(email=email, password=password)
                new_user.username = username
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()
                print new_user
                auth_user = authenticate(email=email, password=password)
                print auth_user
                login(request, auth_user)
                return HttpResponseRedirect('/user_detail_view/%s' % new_user.pk)
            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))
