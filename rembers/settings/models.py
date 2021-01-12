from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Settings(models.Model):

    class FieldType(models.TextChoices):
        STRING = 'STR', _('string')
        INTEGER = 'INT', _('integer')
        BOOLEAN = 'BLN', _('boolean')
        TEXT = 'TXT', _('text')
        UPLOAD = 'FIL', _('file')

    name = models.CharField(unique=True, max_length=191)
    value = models.TextField()
    category = models.CharField(max_length=191)
    field_type = models.CharField(max_length=3, default=FieldType.STRING, choices=FieldType.choices)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def all_as_dict(cls):
        try:
            return [
                {
                    "id": q.id,
                    "name": q.name,
                    "value": q.value,
                    "category": q.category,
                    "field_type": q.field_type,
                    "description": q.description
                } for q in cls.objects.order_by('id')
            ]
        except AttributeError as err:
            raise err.with_traceback(err.__traceback__)

    @classmethod
    def get_one(cls, **kwargs):
        q = cls.objects.filter(**kwargs).first()

        try:
            return {
                "id": q.id,
                "name": q.name,
                "value": q.value,
                "category": q.category,
                "field_type": q.field_type,
                "description": q.description
            }
        except AttributeError as err:
            raise err.with_traceback(err.__traceback__)
