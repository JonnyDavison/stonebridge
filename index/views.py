from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from .models import Home, Gallery, Feature, Review, ContactSubmission, About, Service
from .forms import ContactForm, AboutForm, ServiceForm 
import os

import logging
logger = logging.getLogger(__name__)

class HomePageView(TemplateView):
    template_name = 'index/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home_data = Home.objects.filter(is_active=True).first()
        if home_data:
            logger.debug(f"AWS_STORAGE_BUCKET_NAME: {settings.AWS_STORAGE_BUCKET_NAME}")
            logger.debug(f"hero_image: {home_data.hero_image}")
            context['hero_image_url'] = home_data.hero_image.url if home_data.hero_image else None
            logger.debug(f"hero_image_url: {context['hero_image_url']}")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        
        # Home data
        home_data = Home.objects.filter(is_active=True).first()
        if home_data:
            context['hero_image_url'] = home_data.hero_image.url if home_data.hero_image else None
            context['logo_url'] = home_data.logo.url if home_data.logo else None
        else:
            context['hero_image_url'] = None
            context['logo_url'] = None
        context['home'] = home_data


        
         # Gallery data
        active_gallery = Gallery.objects.filter(is_active=True).first()
        if active_gallery:
            gallery_images = []
            for i in range(1, 13):  # Assuming you have 12 image fields
                image_field = getattr(active_gallery, f'gallery_image{i}')
                if image_field:
                    gallery_images.append(image_field.url)
            context['gallery_images'] = gallery_images
            context['gallery_name'] = active_gallery.name
            context['gallery_description'] = active_gallery.description
        else:
            context['gallery_images'] = []
            context['gallery_name'] = None
            context['gallery_description'] = None

        # Feature data
        feature = Feature.objects.filter(is_active=True).first()
        if feature:
            context['feature_image_url'] = feature.feature_image.url if feature.feature_image else None
            context['feature'] = feature
            context['feature_items'] = feature.items.all()
        else:
            context['feature'] = None
            context['feature_items'] = []

        # Review data
        reviews = Review.objects.all().order_by('-created_at')
        context['reviews'] = reviews

        # Add ContactForm to the context
        context['contact_form'] = ContactForm()

        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            submission = form.save()

            # Send email
            subject = f"New contact form submission: {submission.subject}"
            message = f"Name: {submission.name}\nEmail: {submission.email}\n\nMessage:\n{submission.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]

            send_mail(subject, message, from_email, recipient_list)
            return redirect('contact_success')
        else:
            # If the form is invalid, re-render the page with the form errors
            context = self.get_context_data()
            context['contact_form'] = form
            return self.render_to_response(context)

class ContactView(View):
    template_name = 'index/contact.html'

    def get_context_data(self, **kwargs):
        context = kwargs
        
        # Home data
        home_data = Home.objects.filter(is_active=True).first()
        if home_data:
            context['hero_image_url'] = home_data.hero_image.url if home_data.hero_image else None
            context['logo_url'] = home_data.logo.url if home_data.logo else None
        else:
            context['hero_image_url'] = None
            context['logo_url'] = None
        context['home'] = home_data
        return context
    
    def get(self, request):
        form = ContactForm()
        context = self.get_context_data(contact_form=form)
        return render(request, self.template_name, context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            submission = form.save()

            # Send email
            subject = f"New contact form submission: {submission.subject}"
            message = f"Name: {submission.name}\nEmail: {submission.email}\n\nMessage:\n{submission.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]

            send_mail(subject, message, from_email, recipient_list)

            # Redirect to a thank you page or the same page with a success message
            return redirect('contact_success')
        
        # If form is not valid, re-render the page with form errors
        context = self.get_context_data(contact_form=form)
        return render(request, self.template_name, context)

def contact_success(request):
    return render(request, 'index/contact_success.html')



class ServiceBaseView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = Home.objects.filter(is_active=True).first()
        return context

class ServiceListView(ServiceBaseView, ListView):
    model = Service
    template_name = 'index/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)

class ServiceDetailView(ServiceBaseView, DetailView):
    model = Service
    template_name = 'index/service_detail.html'
    context_object_name = 'service'

class ServiceCreateView(LoginRequiredMixin, UserPassesTestMixin, ServiceBaseView, CreateView):
    model = Service
    template_name = 'index/service_form.html'
    form_class = ServiceForm
    success_url = reverse_lazy('service_list')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.object.image:
            # Print debug information
            print(f"Image saved: {self.object.image.name}")
            print(f"Image URL: {self.object.image.url}")
        return response

class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, ServiceBaseView, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'index/service_form.html'
    success_url = reverse_lazy('service_list')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.object.image:
            # Print debug information
            print(f"Image updated: {self.object.image.name}")
            print(f"Image URL: {self.object.image.url}")
        return response

class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, ServiceBaseView, DeleteView):
    model = Service
    template_name = 'index/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')

    def test_func(self):
        return self.request.user.is_superuser


class AboutBaseView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = Home.objects.filter(is_active=True).first()
        return context

class AboutListView(AboutBaseView, ListView):
    model = About
    template_name = 'index/about.html'
    context_object_name = 'abouts'
    
    def get_queryset(self):
        return About.objects.filter(is_active=True)

class AboutDetailView(AboutBaseView, DetailView):
    model = About
    template_name = 'index/about_detail.html'
    context_object_name = 'about'

@method_decorator(login_required, name='dispatch')
class AboutCreateView(AboutBaseView, CreateView):
    model = About
    template_name = 'index/about_form.html'
    form_class = AboutForm
    success_url = reverse_lazy('about')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class AboutUpdateView(AboutBaseView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = About
    form_class = AboutForm
    template_name = 'index/about_form.html'
    success_url = reverse_lazy('about')

    def test_func(self):
        return self.request.user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class AboutDeleteView(AboutBaseView, DeleteView):
    model = About
    template_name = 'index/about_confirm_delete.html'
    success_url = reverse_lazy('about')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
    
class MenuPageView(TemplateView):
    template_name = 'index/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Home data
        home_data = Home.objects.filter(is_active=True).first()
        if home_data:
            if home_data.hero_image and os.path.isfile(home_data.hero_image.path):
                context['hero_image_url'] = home_data.hero_image.url
            else:
                context['hero_image_url'] = None
            
            if home_data.logo and os.path.isfile(home_data.logo.path):
                context['logo_url'] = home_data.logo.url
            else:
                context['logo_url'] = None
        else:
            context['hero_image_url'] = None
            context['logo_url'] = None
        context['home'] = home_data

        return context
