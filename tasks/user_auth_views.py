import logging
from django.shortcuts import render, redirect, reverse, render_to_response
from django.http import HttpResponseRedirect,HttpResponse, HttpResponseForbidden
from .models import TaskForm, Task, UsernameForm, Username
from django.template import RequestContext

logger = logging.getLogger(__name__)

def sign_in(request):
    try:
        if request.method == 'POST':
            return HttpResponseForbidden('METHOD NOT ALLOWED')

        requestMetaData = request.META
        http_user_agent = requestMetaData.get('HTTP_USER_AGENT')
        findOS = http_user_agent.find("Linux")
        if findOS:
            userOS = "Linux"
        logging.warning(userOS)

        return HttpResponse(f"WOILA, user os is {userOS}")

    except Exception:
        return Exception



def signup(request):
    if request.method == 'POST':
        return HttpResponseForbidden('Forbidden', 403)
    return render(request, 'signupForm.html')
