from django.db import models

# Create your models here.

class Join(models.Model):
	email = models.EmailField()
	friend = models.ForeignKey("self", related_name='referral', \
										null=True, blank=True)
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_adress = models.CharField(max_length=120, default="foo")
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __str__(self):
		return "%s" %(self.ref_id)
		#return str(self.email)

	class Meta:
		unique_together = ("email", "ref_id",)