from django import forms
from django_summernote.widgets import SummernoteWidget
from django.forms import inlineformset_factory
from index.models import Home, Feature, FeatureItem, Gallery, Review, Service, About


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['logo', 'main_title', 'sub_title', 'call_to_action', 'intro', 'intro_title',
                  'hero_image', 'is_active', 'keywords', 'description', 'google_site_verification',
                  'business_name', 'phone_number', 'email', 'address', 'facebook', 'instagram']
        widgets = {
            'main_title': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['para', ['ul', 'ol', 'paragraph']],
                    ],
                }
            }),
            'sub_title': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['para', ['ul', 'ol', 'paragraph']],
                    ],
                }
            }),
            'call_to_action': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['para', ['ul', 'ol', 'paragraph']],
                    ],
                }
            }),
            'intro_title': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['para', ['ul', 'ol', 'paragraph']],
                    ],
                }
            }),
            'intro': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['para', ['ul', 'ol', 'paragraph']],
                    ],
                }
            }),
        }

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['feature_image', 'feature_title', 'feature_sub_title', 'is_active']
        widgets = {
            'feature_title': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['para', ['ul', 'ol', 'paragraph']],
                    ],
                }
            }),
            'feature_sub_title': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                    ],
                }
            }),
        }

class FeatureItemForm(forms.ModelForm):
    class Meta:
        model = FeatureItem
        fields = ['icon', 'title', 'description']
        widgets = {
            'description': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                    ],
                }
            }),
        }

FeatureItemFormSet = inlineformset_factory(
    Feature, FeatureItem, form=FeatureItemForm, extra=1, can_delete=True
)

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'description', 'is_active', 'gallery_image1', 'gallery_image2', 'gallery_image3', 
                  'gallery_image4', 'gallery_image5', 'gallery_image6', 'gallery_image7', 'gallery_image8', 
                  'gallery_image9', 'gallery_image10', 'gallery_image11', 'gallery_image12']
        widgets = {
            'description': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['para', ['ul', 'ol', 'paragraph']],
                    ],
                }
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            if field_name.startswith('gallery_image'):
                self.fields[field_name].widget.attrs.update({'class': 'form-control-file'})
                

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment', 'image']
        widgets = {
            'comment': SummernoteWidget(attrs={
                'summernote': {
                    'height': '300px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['para', ['ul', 'ol', 'paragraph']],
                    ],
                }
            }),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'sub_title', 'description', 'price', 'image']
        widgets = {
            'description': SummernoteWidget(attrs={
                'summernote': {
                    'height': '200px',
                    'toolbar': [
                        ['style', ['bold', 'italic', 'underline', 'clear']],
                        ['font', ['strikethrough', 'superscript', 'subscript']],
                        ['insert', ['link', 'picture']],
                    ],
                }
            }),
        }

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'sub_title', 'content', 'image']
        widgets = {
            'content': SummernoteWidget(attrs={
                'summernote': {
                    'height': '400px',
                }
            }),
        }    
        
# class GalleryForm(forms.ModelForm):
#     class Meta:
#         model = Gallery
#         fields = [
#             'name', 
#             'description', 
#             'is_active', 
#             'gallery_image1', 
#             'gallery_image2', 
#             'gallery_image3', 
#             'gallery_image4', 
#             'gallery_image5', 
#             'gallery_image6', 
#             'gallery_image7', 
#             'gallery_image8', 
#             'gallery_image9', 
#             'gallery_image10', 
#             'gallery_image11', 
#             'gallery_image12'
#         ]
#         widgets = {
#             'description': SummernoteWidget(),
#             'gallery_image1': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image2': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image3': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image4': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image5': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image6': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image7': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image8': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image9': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image10': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image11': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'gallery_image12': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }

#     def clean_gallery_image1(self):
#         return self._clean_image('gallery_image1')

#     def clean_gallery_image2(self):
#         return self._clean_image('gallery_image2')

#     def clean_gallery_image3(self):
#         return self._clean_image('gallery_image3')

#     def clean_gallery_image4(self):
#         return self._clean_image('gallery_image4')

#     def clean_gallery_image5(self):
#         return self._clean_image('gallery_image5')

#     def clean_gallery_image6(self):
#         return self._clean_image('gallery_image6')

#     def clean_gallery_image7(self):
#         return self._clean_image('gallery_image7')

#     def clean_gallery_image8(self):
#         return self._clean_image('gallery_image8')

#     def clean_gallery_image9(self):
#         return self._clean_image('gallery_image9')

#     def clean_gallery_image10(self):
#         return self._clean_image('gallery_image10')

#     def clean_gallery_image11(self):
#         return self._clean_image('gallery_image11')

#     def clean_gallery_image12(self):
#         return self._clean_image('gallery_image12')

#     def _clean_image(self, field_name):
#         image = self.cleaned_data.get(field_name)
#         if image:
#             if image.size > 5 * 1024 * 1024:  # 5MB limit
#                 raise forms.ValidationError(f"{field_name}: Image file too large ( > 5MB )")
#             if image.content_type not in ['image/jpeg', 'image/png', 'image/gif']:
#                 raise forms.ValidationError(f"{field_name}: Please upload a JPEG, PNG or GIF image.")
#         return image
    
