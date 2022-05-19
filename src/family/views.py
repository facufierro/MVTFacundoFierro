from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from family.models import family_member
from django.http import HttpResponse
# Create your views here.


def index(request):
    family_members = family_member.objects.all()
    template = loader.get_template('index.html')
    context = {'family_members': family_members, }
    return HttpResponse(template.render(context, request))


def create(request):
    pass


def update():
    pass


def delete():
    pass
