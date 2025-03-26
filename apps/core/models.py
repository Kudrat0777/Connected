from django.db import models

# Create your models here.

class Employee(models.Model) :
    image = models.ImageField(upload_to="img/", verbose_name="Rasm")
    full_name = models.CharField(max_length=50, verbose_name="Ism")
    role = models.CharField(max_length=50, verbose_name="Mutaxassisligi")
    
    def __str__(self):
        return self.full_name
    
    class Meta :
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar"
        
class About(models.Model) :
    title = models.TextField(verbose_name = "Haqida")
    subtitle = models.CharField(max_length=255, verbose_name="Qisqacha")
    
    def __str__(self):
        return self.title
    
    class Meta :
        verbose_name = "Haqida"
        verbose_name_plural = "Biz haqimizda"
        
        
class Contact(models.Model) :
    phone = models.CharField(max_length=30, verbose_name="Telefon raqam")
    email = models.EmailField(verbose_name="Email")
    location = models.TextField(verbose_name="Manzil")
    
    def __str__(self):
        return self.location
    
    class Meta :
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontaktlar"
        
