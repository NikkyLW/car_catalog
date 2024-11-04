from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from cars.models import Car

class IndexView(ListView):
    template_name = 'main/index.html'
    model = Car
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset()
        return cars
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "Текст о том почему этот магазин такой классный, и какой хороший товар."
        return context