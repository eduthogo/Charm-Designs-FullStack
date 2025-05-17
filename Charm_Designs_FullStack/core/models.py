from django.db import models

# Create your models here.
class Logo(models.Model):
    logo = models.ImageField(upload_to='logo_images/')
    favicon = models.ImageField(upload_to='favicon_images/')

    class Meta:
        verbose_name_plural = "Logo"

class HeroPage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hero_images/')
    worked_with = models.TextField(help_text="Enter company names separated by commans or new lines", blank=True)

    class Meta:
        verbose_name_plural = "Hero Page"


class Benefits(models.Model):
    benefits = models.CharField(max_length=200)
    description = models.TextField(help_text="Enter a short description of the beneifits", blank=True)
    image = models.ImageField(upload_to='benefits_images/')

    class Meta:
        verbose_name_plural = "Benefits"


class Services(models.Model):
    service_name = models.CharField(max_length=200)
    description = models.TextField(help_text="Enter a short description of the service", blank=True)
    image = models.ImageField(help_text="Upload the image that will be used on the homepage", upload_to='services_images/')

    class Meta:
        verbose_name_plural = "Services"


class GalleryImages(models.Model):
    image=models.ImageField(help_text="These are the images that are going to be displayed on the homepage gallery section", upload_to='homepage_gallery_images/')

    class Meta:
        verbose_name_plural = "Gallery Images"


class Testimonials(models.Model):
    person_name = models.CharField(max_length=200)
    person_title = models.CharField(max_length=200)
    testimonial = models.TextField(help_text="Enter a short testimonial", blank=True)

    class Meta:
        verbose_name_plural = "Testimonials"


class AboutUs(models.Model):
    description = models.TextField(help_text="Enter a testimonial", blank=True)
    image = models.ImageField(upload_to="about_us_images/")

    class Meta:
        verbose_name_plural = "About Us"


class ContactUs(models.Model):
    image = models.ImageField(upload_to="contact_us_images/")

    class Meta:
        verbose_name_plural = "Contact Us"


class Footer(models.Model):
    phone_number = models.CharField(max_length=200)
    email = models.EmailField(max_length= 200)

    class Meta:
        verbose_name_plural = "Footer"


class SocialIcons(models.Model):
    image = models.ImageField(upload_to="social_icons/")

    class Meta:
        verbose_name_plural = "Social Icons"


class Gallery(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='gallery_images/')

    class Meta:
        verbose_name_plural = "Gallery"

