from django.shortcuts import render
from .models import HeroPage, Logo, Benefits, Services, GalleryImages, Testimonials, AboutUs, ContactUs, Footer, SocialIcons, Gallery

# Create your views here.

# This is the global context processor that will be used to add the logo and favicon to all templates
def global_context(request):
    return {
        # Logo
        'logo': Logo.objects.first(), 
        # Favicon
        'favicon': Logo.objects.first(),

        # Footer Section
        'footer' : Footer.objects.first(),
        'social_icons' : SocialIcons.objects.all()
    }


def index(request):
    context = {
        # Hero Page Section
        'hero' : HeroPage.objects.first(),

        #Benefits Section
        'benefits' : Benefits.objects.all(),

        #Services Section
        'services' : Services.objects.all(),

        #GalleryImage Section
        'gallery_images' : GalleryImages.objects.all(),

        #Testimonials Section
        'testimonials' : Testimonials.objects.all(),

        #About Us Section
        'about_us' : AboutUs.objects.first(),

        #Contact Us Section
        'contact_us' : ContactUs.objects.first(),
    }

    return render(request, 'index.html', context)


def gallery(request):

    # Gallery Section
    gallery = Gallery.all()
    return render(request, 'gallery.html')