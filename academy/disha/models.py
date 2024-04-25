from django.db import models
import uuid
from django.utils import timezone

class OfficeStaff(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    profile = models.ImageField(null=True, blank=True, upload_to="office_staff_profiles/")
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact_one = models.CharField(max_length=20)
    contact_two = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=700)
    joined_date = models.DateField(null=True, blank=True)
    
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name