from django import template
from orders.models import Order,OrderItem
from django.db import models

register = template.Library()

@register.simple_tag
def get_product_sales(product):
    """Return the number of orders with the product sold and delivered."""
    # Assuming `OrderItem` is the model related to the product
    return Order.objects.filter(
        items__product=product,
        payment_status='delivered'
    ).count()

@register.simple_tag
def total_revenue(product):
    """Return the total revenue generated from the product sold and delivered."""
    # Assuming `OrderItem` is the model related to the product
    total_revenue = OrderItem.objects.filter(
        product=product,
        order__payment_status='delivered'
    ).aggregate(
        total_revenue=models.Sum(models.F('total_price'))
    )['total_revenue']

    # Return formatted total revenue or 0 if None
    return f"{total_revenue:,.0f} IQD" if total_revenue else 0