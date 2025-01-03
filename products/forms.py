from django import forms
from .widgets import CustomClearableFileInput, CustomMultipleImageInput
from .models import Product, Category, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['slug', 'rating']  # These fields are typically auto-generated or calculated
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'best_before': forms.DateInput(attrs={'type': 'date'}),
        }

    image = forms.ImageField(label='Main Image', required=False, widget=CustomClearableFileInput)
    
    # Add a field for multiple product images
    additional_images = forms.FileField(
        label='Additional Images',
        widget=CustomMultipleImageInput,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'profile-form text-muted'

        # Add placeholders and classes
        placeholders = {
            'sku': 'SKU',
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Price',
            'offer_price': 'Offer Price (if applicable)',
            'weight': 'Weight (kg)',
            'stock_quantity': 'Stock Quantity',
            'farm_source': 'Farm Source',
        }

        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
            # Handle additional images
            if self.cleaned_data.get('additional_images'):
                for image in self.cleaned_data['additional_images']:
                    ProductImage.objects.create(product=product, image=image)
        return product

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']
    
    image = forms.ImageField(label='Image', required=True, widget=CustomClearableFileInput)
