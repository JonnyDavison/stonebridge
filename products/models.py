from django.db import models
from django.utils.text import slugify

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

TAG_CHOICES = (
    ('N', 'NEW'),
    ('L', 'LOW STOCK'),
    ('P', 'ON SALE'),
    ('S', 'SOLD OUT')
)

class Category(models.Model):
    """ Category model """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """ Product model """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, null=True, blank=True)
    tag = models.CharField(choices=TAG_CHOICES, max_length=1, null=True, blank=True)
    slug = models.SlugField(max_length=254, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, help_text="Weight in kg")
    stock_quantity = models.IntegerField(default=0)
    farm_source = models.CharField(max_length=254, null=True, blank=True)
    best_before = models.DateField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    related_products = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.stock_quantity < 0:
            self.stock_quantity = 0
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} Image"
