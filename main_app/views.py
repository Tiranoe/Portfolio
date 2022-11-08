from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView
from .models import Project
from django.views.generic import DetailView
from .forms import ContactForm

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class ProjectList(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context

class ProjectDetail(DetailView):
    model = Project
    template_name = "project_detail.html"

class Contact(TemplateView):
    template_name = "contact.html"

def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)