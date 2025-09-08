from django.db import models
import uuid

# Create your models here.
class Service(models.Model):
    title =models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='default.jpg')

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        

class ServiceInquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, null=True, blank=True)
    message = models.TextField()
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name="inquiries")

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} → {self.service.title}"
