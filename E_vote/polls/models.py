from django.db import models

# Create your models here.
class Choice(models.Model):
	Choice_text = models.CharField(max_length = 200)
	candidate_number =  models.IntegerField()
	candidate_image = models.ImageField(null = True, blank= True)
	vote = models.IntegerField(default = 0)

	
	def __str__(self):
		return self.Choice_text

