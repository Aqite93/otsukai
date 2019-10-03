from django.db import models
from accounts.models import User


class Errand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    errand_id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=1024,
                                   blank=True,
                                   help_text='依頼内容を記載してください．')

    class Meta:
        db_table = 'errand'
