from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="aboutme"),
    path('projects/', views.ProjectList.as_view(), name="project_list"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project_detail"),
    path('contact/', views.Contact.as_view(), name="contact me"),
]