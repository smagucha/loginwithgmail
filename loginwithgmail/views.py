from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return HttpResponse( '<p>hello world </p>')

@login_required
def testlogin(request):
    return render(request, 'loginwithgmail/home.html')


