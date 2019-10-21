from django.db import models
from accounts.models import User
from otsukai.models import Category


class Errand(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    price = models.IntegerField()
    image = models.FileField(name='image')
    description = models.TextField(blank=True,
                                   max_length=1000,
                                   help_text='依頼内容を記載してください．')

    class Meta:
        db_table = 'errand'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
