from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(
        max_length=20
    )

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.description
