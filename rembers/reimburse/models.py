from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Reimburse(models.Model):
    class DocumentType(models.TextChoices):
        PDF = 'PDF', _('document/pdf')
        JPG = 'JPG', _('image/jpg')
        PNG = 'PNG', _('image/png')

    class CategoryType(models.TextChoices):
        transport = 'transport', _('Transport')
        food_and_beverage = 'food_and_beverage', _('Food and beverage')
        office_supplies = 'office_supplies', _('Office supplies')
        other = 'other', _('other')

    class StatusType(models.TextChoices):
        submitted = 'submitted', _('Submitted')
        on_progress = 'on_progress', _('on_progress')
        completed = 'completed', _('completed')
        rejected = 'rejected', _('rejected')

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date = models.DateField()
    document_attach = models.FileField(upload_to="upload")
    document_type = models.CharField(max_length=3, default=DocumentType.JPG, choices=DocumentType.choices)
    description = models.TextField(null=True)
    category = models.CharField(max_length=20, default=CategoryType.transport, choices=CategoryType.choices)
    status = models.CharField(max_length=20, default=StatusType.submitted, choices=StatusType.choices)
    amount = models.DecimalField(max_length=25, max_digits=25, decimal_places=0)
    remarks = models.TextField(null=True)

    @classmethod
    def all_as_dict(cls):
        return [
            {
                "id": q.id,
                "date": q.date.strftime('%Y/%m/%d'),
                "document_attach": q.document_attach.url,
                "document_type": q.document_type,
                "description": q.description,
                "category": q.category
            } for q in cls.objects.order_by('id')
        ]

    @classmethod
    def get_one(cls, **kwargs):
        q = cls.objects.filter(**kwargs).first()
        return {
            "id": q.id,
            "date": q.date.strftime('%Y/%m/%d'),
            "document_attach": q.document_attach.url,
            "document_type": q.document_type,
            "description": q.description,
            "category": q.category
        }
