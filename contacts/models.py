from django.db import models
import uuid

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(
                primary_key=True,
                default=uuid.uuid4,
                editable=False
            )
    name = models.CharField(max_length=200, required=False)
    email = models.CharField(max_length=330, required=False)
    phone = models.IntegerField(max_length=14, required=False)

    def __str__(self):
        return f'{self.name}'
