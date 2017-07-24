from django.shortcuts import render

def index(request):
    context = {}
    template = "home.html"
    return render(request, template, context)