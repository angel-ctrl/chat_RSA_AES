from django.views.generic import ListView
from django.shortcuts import render
import jwt

def main(request):
    context = {}

    token = request.COOKIES.get('token')

    decoded = jwt.decode(token, options={"verify_signature": False})

    context['username'] = decoded['name']

    return render(request, 'hola_test.html', context)

def login(request):
    context = {}

    context['car'] = "hola"

    return render(request, 'demo-login.html', context)