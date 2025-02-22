from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),

    # App-level URLs
    path('', include('index.urls')),  # Homepage
    path('dashboard/', include('dashboard.urls')),  # Admin dashboard for users
    path('profiles/', include('profiles.urls')),  # User profiles
    path('products/', include('products.urls')),  # Products app (e-commerce)
    path('bag/', include('bag.urls')),  # Shopping bag/basket app
    # path('checkout/', include('checkout.urls')),  # Checkout/payment app
    # path('orders/', include('orders.urls')),  # Orders app

    # Other URLs
    path('cookies/', include('cookie_consent.urls')),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handlers
handler404 = 'core.views.handler404'

