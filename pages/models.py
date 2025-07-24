from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


class ContactModel(BaseModel):
    name = models.CharField(max_length=123)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=13, null=True, blank=True
        )
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} | {self.email}"
    

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"