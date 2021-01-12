from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=171)
    bank_name = models.CharField(max_length=191, null=True)
    bank_account = models.CharField(max_length=191, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    phone_number = models.CharField(max_length=191)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_accounts(cls, user_id):
        q = cls.objects.filter(user_id=User(pk=user_id)).first()

        try:
            return {
                "id": q.user.id,
                "username": q.user.username,
                "name": q.name,
                "profile_picture": q.profile_picture.url,
                "phone_number": q.phone_number,
                "bank_name": q.bank_name,
                "bank_account": q.bank_account,
                "description": q.description
            }
        except AttributeError as err:
            raise err.with_traceback(err.__traceback__)
