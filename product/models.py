from django.db import models
import uuid


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to="products/",blank=True, null=True)
    features = models.TextField(blank=True, null=True, help_text="Enter features separated by line breaks")
    use_cases = models.TextField(blank=True, null=True, help_text="Enter use cases separated by line breaks")

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)

    def __str__(self):
        return self.title

    
    class Meta:
        ordering = ['title']

class ProductInquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, null=True, blank=True)
    message = models.TextField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="inquiries")

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} → {self.product.title}"