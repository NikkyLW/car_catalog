from pyexpat.errors import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from cars.forms import CarCreate
from cars.models import Car
from comments.forms import CommentCreate
from comments.models import Comment
from common.mixins import CacheMixin


class CarUpdateView(CacheMixin , UpdateView):
    template_name = 'cars/update.html'
    form_class = CarCreate
    success_url = reverse_lazy('index:main')

    def get_object(self, queryset=None):
        car = Car.objects.get(pk=self.kwargs['pk'])
        return car
    
    def form_valid(self, form):
        self.success_url = reverse_lazy('car:update', kwargs={'pk': self.kwargs['pk']})

        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Карточка автомобиля'

        return context

class CarCreateView(CreateView):
    template_name = 'cars/create.html'
    form_class = CarCreate

    def form_valid(self, form):
        car = form.instance

        if car:
            form = form.save(commit=False)
            form.owner = self.request.user
            form.save()

        return HttpResponseRedirect(
            reverse_lazy('car:my_cars')
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление автомобиля'
        return context

class MyCarView(ListView):
    model = Car
    template_name = "cars/my_cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset()
        cars = cars.filter(owner=self.request.user)
        return cars
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Мои автомобили"
        return context
    
class CarCardView(DetailView, CreateView):
    template_name = "cars/card.html"
    context_object_name = "car"
    form_class = CommentCreate
    
    def get_object(self, queryset=None):
        car = Car.objects.get(pk=self.kwargs['pk'])
        return car
    
    def get_comments(self):
        comments = Comment.objects.filter(car=self.kwargs['pk'])
        return comments
    
    def form_valid(self, form):
        comment = form.instance
        car = self.get_object()

        if comment:
            comment = form.save(commit=False)
            comment.author = self.request.user
            comment.car = car
            comment.save()

        return HttpResponseRedirect(
            reverse_lazy('car:card_car', kwargs={'pk': car.id})
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Карточка'
        context["comments"] = self.get_comments()
        return context

def carDelete(request, pk):
    Car.objects.filter(id=pk).delete()
    return redirect(reverse('car:my_cars'))