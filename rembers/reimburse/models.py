import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Reimburse(models.Model):
    class DocumentType(models.TextChoices):
        PDF = 'PDF', _('document/pdf')
        JPG = 'JPG', _('image/jpg')
        PNG = 'PNG', _('image/png')

    id = models.AutoField(primary_key=True)
    date = models.DateField()
    document_attach = models.FileField(upload_to="upload")
    document_type = models.CharField(max_length=3, default=DocumentType.JPG, choices=DocumentType.choices)
    description = models.TextField()

    @classmethod
    def all_as_dict(cls):
        return [
            {
                "id": q.id,
                "date": q.date.strftime('%Y/%m/%d'),
                "document_attach": q.document_attach.url,
                "document_type": q.document_type,
                "description": q.description
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
            "description": q.description
        }
