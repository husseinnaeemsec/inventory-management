from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from . import models
from django.db.models import Sum,Q
from .forms import CreateProductForm,ProducImageModelForm
from django.http import JsonResponse
# Create your views here.
class ProductsList(ListView):
    model = models.Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    ordering = ['-created_at']
    paginate_by = 10
        
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering',None)
        filter = self.request.GET.get('filter',None)
        # Check if ordering by sales is requested
        if ordering is not None:
            if self.request.GET.get("ordering") == 'sales':
                # Annotate each product with total sales (revenue) from OrderItems
                queryset = queryset.annotate(
                    total_sales=Sum('orders_items__total_price', filter=Q(orders_items__order__payment_status='delivered'))
                ).order_by('-total_sales')  # Order by total_sales in descending order
            elif ordering == 'price':
                queryset = queryset.order_by('-price')  # Order by price in ascending order
            elif ordering == 'category':
                queryset = queryset.order_by('category__name')  # Order by category name in ascending order
            else:
                queryset = queryset.order_by('name')  # Default ordering by creation date in descending order
        
        if filter is not None:
            if filter == 'outof_stock':
                queryset = queryset.filter(quantity=0)  # Filter by selected category
            if filter == 'stock_alert':
                queryset = queryset.filter(quantity__lt=10)  # Filter by selected category
        
        return queryset


class CreateProduct(CreateView):
    model = models.Product
    form_class = CreateProductForm
    template_name = 'products/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        
        return context
    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        form = CreateProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            for image in images:
                models.ProductImage.objects.create(product=product, image=image)
            return JsonResponse({'success': True, 'message': 'Product added successfully.'})