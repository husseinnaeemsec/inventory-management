from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from . import models
class OrdersList(ListView):
    model = models.Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'
    paginate_by = 10
    