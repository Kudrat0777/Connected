from django.db import models

class Service(models.Model):
    title = models.CharField("Название услуги", max_length=100),
    description = models.TextField("Описание")

    def __str__(self) -> str:
        return self.title
    

class ContactRequest(models.Model):
    name = models.CharField("Имя", max_length=50)
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    message = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Заявка от {self.name}"
           
