from django.db import models
import uuid



class Contact(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    
    def __str__(self):
        return self.name


class Careers(models.Model):
    EMPLOYMENT_TYPES = [
        ('FT', 'تمام وقت'),
        ('PT', 'پاره وقت'),
        ('PR', 'پروژه‌ای'),
        ('IN', 'کارآموزی'),
    ]

    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    position = models.CharField(max_length=200,null=True,blank=True)
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)
    employment_type = models.CharField(max_length=2,
        choices=EMPLOYMENT_TYPES,
        default='FT', )
    location = models.CharField(max_length=100, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    
    def __str__(self):
        return self.name