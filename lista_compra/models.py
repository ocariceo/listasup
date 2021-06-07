from django.db import models

# Create your models here.

class Compra(models.Model):
	producto = models.CharField(max_length=200)
	completo = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.producto
