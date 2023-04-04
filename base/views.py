from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name='main/index.html'

home_runner=HomeView.as_view()    

class ProfileView(TemplateView):
    template_name='main/profile.html'

profile_runner=ProfileView.as_view()    