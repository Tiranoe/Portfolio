from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Project:
    def __init__(self, name, image, tool, description):
        self.name = name
        self.image = image
        self.tool = tool
        self.description = description

projects = [
    Project("Most recent Project", 
    "https://github.com/Tiranoe/adventureTime/blob/main/assets/adventuretimegif.gif?raw=true", 
    "Python, Django", 
    "Community Applications for travelers to share their unique experiences"),
]

class ProjectList(TemplateView):
    template_name = "project_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = projects
        return context

class Contact(TemplateView):
    template_name = "contact.html"