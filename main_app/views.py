from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from .models import Project

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Project:
    def __init__(self, name, image, tool, description, github, live):
        self.name = name
        self.image = image
        self.tool = tool
        self.description = description
        self.github = github
        self.live = live

class ProjectList(TemplateView):
    template_name = "project_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class Contact(TemplateView):
    template_name = "contact.html"