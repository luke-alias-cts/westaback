from django.db import models

# Create your models here.

class Comment(models.Model):
    user           = models.CharField(max_length = 50)
    comment        = models.CharField(max_length = 500)
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'Comment'