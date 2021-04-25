from django.db import models as _

# Create your models here.


class Guest(_.Model):
    name  = _.CharField(max_length=50)
    email = _.CharField(max_length=50, unique=True)
    phone = _.CharField(max_length=50, unique=True)
    file  = _.FileField(upload_to='uploads')
    created_at = _.DateTimeField(auto_now_add=True)
    updated_at = _.DateTimeField(auto_now=True)
