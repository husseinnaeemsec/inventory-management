from django import forms
from .models import Product,ProductImage
class CreateProductForm(forms.ModelForm):
    
    def __init__(self,*args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)
        
        for field_name,field in self.fields.items():
            field.widget.attrs['class'] = 'w-full bg-gray-50 border my-2'
    
    
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'quantity',
            'description',
            'category',
            'discount',
            'discount_type',
        ]

class ProducImageModelForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']