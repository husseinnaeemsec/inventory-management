from django.db import models

class Order(models.Model):
    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    customer = models.ForeignKey('users.Customer',on_delete=models.SET_NULL,null=True,related_name='orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=255)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    tracking_number = models.CharField(max_length=200, blank=True, null=True)
    payment_status = models.CharField(max_length=200, blank=True, null=True,choices=PAYMENT_STATUS)
    notes = models.TextField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    delivery_note = models.TextField(blank=True, null=True)
    delivered_by = models.CharField(max_length=200, blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)

    def get_total(self):
        return f"{self.total_amount:,.0f} IQD"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE,related_name='orders_items')
    variation = models.ForeignKey('products.Variation', on_delete=models.CASCADE, related_name='orders_items',blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

