from django.db import models

# Create your models here.
class Choice(models.Model):
	candidate_name       =  models.CharField(max_length =  200)
	carrier_history      =  models.CharField(max_length = 400,null = True)
	candidate_status     =  models.CharField (max_length =200,null=True)
	candidate_email      =  models.CharField(max_length =  200 , null = True)
	candidate_date_birth =  models.DateField(null       = True)
	candidate_number     =  models.IntegerField()
	candidate_tel        =  models.IntegerField( default = 0)
	candidate_image      =  models.ImageField(upload_to ='img/',null   = True, blank  = True)
	candidate_role       =  models.CharField(max_length = 200,  null     = True)
	vote                 =  models.IntegerField(default = 0)

	
	def __str__(self):
		return self.candidate_name

