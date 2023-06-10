# What is going to be 'invoked' when a user visits your website?
from django.views.generic import TemplateView


# fancy way of using templates
class HomePageView(TemplateView):
    template_name = 'home.html'

