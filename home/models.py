from django.db import models


class Contact(models.Model):
    """ models and fields for contact model"""
    subject = models.CharField(max_length=130, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.subject
