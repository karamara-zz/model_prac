from django.db import models

# Create your models here.
class Interest(models.Model):
	name = models.TextField(max_length = 45)
	created_at = models.DateTimeField()
	class Meta:
		db_table = "interests"
class User(models.Model):
	first_name = models.TextField(max_length = 45)
	last_name = models.TextField(max_length = 45)
	age = models.IntegerField()
	created_at = models.DateTimeField()
	occupation = models.TextField(max_length = 45)
	interest_id = models.ForeignKey(Interest)
	class Meta:
		db_table = "users"