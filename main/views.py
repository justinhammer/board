from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic.detail import DetailView

from main.models import CustomUser
# Create your views here.


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_detail_view.html'
    slug_field = 'user_name'
