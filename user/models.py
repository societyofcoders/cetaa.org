from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

LO_CHOICES = (
	(1,'YES'),
	(0,'NO'),
)

DEP_CHOICES = (
	('ME','MECHANICAL ENGINEERING'),
	('CE','CIVIL ENGINEERING'),
	('EE','ELECTRICAL ENGINEERING'),
	('CS','COMPUTER SCIENCE ENGINEERING'),
	('EC','ELECTRONICS AND COMMUNICATION ENGINEERING'),
	('AR','ARCHITECTURAL ENGINEERING'),

)

SEX = (
	('M','MALE'),
	('F','FEMALE'),

)

LEVELS = {
	(0, 'Normal User'),
	(1, 'Sub Editor'),
	(2, 'Editor'),
	(3, 'Database Manager'),
	(100, 'Super Admin'),
	(-1,'Blocked')
}

VERIFICATION = {
	(0, 'Email Verification pending'),
	(1, 'Unverified'),
	(2, 'Verification pending'),
	(3, 'Verified')
}

class User(models.Model):
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	sex = models.CharField(max_length=1, choices=SEX)
	dob = models.DateField(blank=False)
	passyear = models.IntegerField(blank=False,validators=[
		MaxValueValidator(2050),
		MinValueValidator(1939)
		])
	address	= models.CharField(max_length=60)
	dept = models.CharField(max_length=2, choices=DEP_CHOICES)
	cur_job	= models.CharField(max_length=30)
	email = models.CharField(max_length=40)
	phone = models.CharField(max_length=15)
	contact	= models.IntegerField(max_length=1,choices=LO_CHOICES)			
#	username = models.CharField(max_length=20,unique=True)
	password = models.CharField(max_length=32)
	prof_pic =models.ImageField(upload_to='static/user_img',blank=True)
	admn_no = models.CharField(max_length=10)
	level = models.IntegerField(choices=LEVELS)
	verification = models.IntegerField(choices=VERIFICATION)


	def __unicode__(self):
		return self.fname +' '+ self.lname