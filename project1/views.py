from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
import datetime

def home(request) :
    return render(request, 'lawyered/index.html')