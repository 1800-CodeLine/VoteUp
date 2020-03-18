from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def on_page_load(request, cookie_ids=[]):
    page_data = {}
    for cookie_id in cookie_ids + ["id"]:
        page_data[cookie_id] = request.COOKIES.get(cookie_id, None)
    page_data["logged_in"] = page_data["id"] is not None
    return page_data

def render_template(request, template_name, context={}, cookies={}, cookies_to_delete=[]):
    response = render(request, template_name, context)
    for cookie_id in cookies:
        response.set_cookie(cookie_id, cookies[cookie_id])
    for cookie_id in cookies_to_delete:
        response.delete_cookie(cookie_id)
    return response

def redirect_to(redirect_url, cookies={}, cookies_to_delete=[]):
    response = redirect(redirect_url)
    for cookie_id in cookies:
        response.set_cookie(cookie_id, cookies[cookie_id])
    for cookie_id in cookies_to_delete:
        response.delete_cookie(cookie_id)
    return response

def base_function(request):
    template_name = "VotingMachine/layout.html"
    load_data = on_page_load(request)
    context = {
        "title": "Page Title"
    }
    cookies = {}
    cookies_to_delete = [] 
    redirect_url = "/" if load_data["logged_in"] else None
    if redirect_url is None:
        return render_template(request, template_name, context, cookies, cookies_to_delete)
    else:
        return redirect_to(redirect_url, cookies, cookies_to_delete)

# Create your views here.
def homepage(request):
    template_name = "VotingMachine/homepage.html"
    load_data = on_page_load(request)
    context = {
        "title": "Home"
    }
    cookies = {}
    cookies_to_delete = [] 
    redirect_url = "/" if load_data["logged_in"] else None
    if redirect_url is None:
        return render_template(request, template_name, context, cookies, cookies_to_delete)
    else:
        return redirect_to(redirect_url, cookies, cookies_to_delete)
