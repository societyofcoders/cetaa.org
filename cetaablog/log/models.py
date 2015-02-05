#from django.db import models

# Create your models here.
from django.db import models
from django.db import forms
from django.forms import extras


LO_CHOICES = (
	('Y','YES'),
	('N','NO'),
)

DEP_CHOICES = (
	('ME','MECHANICAL ENGINEERING'),
	('CE','CIVIL ENGINEERING'),
	('EE','ELECTRICAL ENGINEERING'),
	('CS'.'COMPUTER SCIENCE ENGINEERING'),
	('EC','ELECTRONICS AND COMMUNICATION ENGINEERING'),
	('AR','ARCHITECTURAL ENGINEERING'),

)

SEX = (
	('M','MALE'),
	('F','FEMALE'),

)


# Create your models here.
class Log(models.Model):
	first_name				=models.CharField(max_length=30)
	last_name				=models.CharField(max_length=30)
	sex						=modles.CharField(max_length=1, choices=SEX)
	birthdate				=forms.DateField(widget=extras.SelectDateWidget)
	passyear				=forms.DateField(widget=extras.SelectDateWidget)
	address					=models.CharField(max_length=60)
	field_of				=models.CharField(max_length=50)
	dept					=models.CharField(max_length=2, choices=DEP_CHOICES)
	cur_job					=models.CharField(max_length=30)
	e_id					=models.CharField(max_length=40)
	ph_no					=models.CharField(max_length=15)
	contact					=models.CharField(max_length=1, choices=LO_CHOICES)			
	user_name				=modles.CharField(max_length=20)
	pas_word				=models.CharField(max_length=32)
	profile_picture			=modles.ImageField(upload_to='thumbpath' blank=True)
	admn_mo					=models.CharField('max_length=10')


	def __unicode__(self):
		return self.user_name
		
