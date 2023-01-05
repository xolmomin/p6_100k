from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'apps/index.html'
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'apps/main_page.html'
