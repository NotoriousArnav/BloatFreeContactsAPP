from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(
                primary_key=True,
                default=uuid.uuid4,
                editable=False
            )
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=330)
    phone = models.IntegerField(max_length=14)

    def __str__(self):
        return f'{self.name}'
