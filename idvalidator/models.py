from django.db import models
from django.utils import timezone

from idvalidator.validators import validate_business_id


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    business_id = models.CharField(max_length=8, validators=[validate_business_id])

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s - %s" % (self.name, self.business_id)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
