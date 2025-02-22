from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm
from index.models import Home, Service, Gallery, Review, ContactSubmission, About, Feature, FeatureItem


def all_products(request):
    """A view to return all Products page with sorting and search"""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    home = Home.objects.filter(is_active=True).first()
   
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}' if sort and direction else None

    # Pagination
    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'home': home,
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """A view to return Product detail page"""
    home = Home.objects.filter(is_active=True).first()
    product = get_object_or_404(Product, pk=product_id)
    
    # Fetch related products based on the same category or other criteria
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]  # Get up to 4 related products excluding the current product
    
    additional_images = product.images.all()  # Fetch additional images associated with the product

    context = {
        'home': home,
        'product': product,
        'related_products': related_products,
        'additional_images': additional_images,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """Add a product to the store"""
    home = Home.objects.filter(is_active=True).first()
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            if 'additional_images' in request.FILES:
                for image in request.FILES.getlist('additional_images'):
                    ProductImage.objects.create(product=product, image=image)
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'home': home,
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    home = Home.objects.filter(is_active=True).first()
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            if 'additional_images' in request.FILES:
                for image in request.FILES.getlist('additional_images'):
                    ProductImage.objects.create(product=product, image=image)
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'home': home,
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))
    
    home = Home.objects.filter(is_active=True).first()
    product = get_object_or_404(Product, pk=product_id)
    
    # Delete associated images before deleting the product (optional)
    product.images.all().delete()  # Delete all additional images associated with the product (if needed)
    
    product.delete()
    
    messages.success(request, 'Product deleted!')
    
    return redirect(reverse('products'))

@login_required
def add_product_image(request, product_id):
    """Add an additional image to a product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    home = Home.objects.filter(is_active=True).first()
    
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            image = form.save(commit=False)
            image.product = product
            image.save()
            
            messages.success(request, 'Successfully added image!')
            
            return redirect(reverse('product_detail', args=[product.id]))
        
        else:
            messages.error(request, 'Failed to add image. Please ensure the form is valid.')
    
    else:
        form = ProductImageForm()

    template = 'products/add_product_image.html'
    
    context = {
        'home': home,
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product_image(request, image_id):
    """Delete an additional image from a product"""
    
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        
        return redirect(reverse('home'))

    image = get_object_or_404(ProductImage, pk=image_id)
    
    product = image.product
   
    image.delete()
   
    messages.success(request, 'Image deleted!')
   
    return redirect(reverse('product_detail', args=[product.id]))


def all_categories(request):
    """A view to return all categories"""
    categories = Category.objects.all()
    home = Home.objects.filter(is_active=True).first()
    context = {
        'home': home,
        'categories': categories,
    }
    return render(request, 'products/categories.html', context)


def category_products(request, category_slug):
    """Display products for a specific category"""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    home = Home.objects.filter(is_active=True).first()
    
    context = {
        'home': home,
        'category': category,
        'products': products,
    }

    return render(request, 'products/category_products.html', context)

