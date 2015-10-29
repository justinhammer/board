from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic.detail import DetailView

from main.models import User
# Create your views here.


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail_view.html'
    slug_field = 'user_name'
