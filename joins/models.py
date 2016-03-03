from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.EmailField()
	referrer = models.ForeignKey("self", related_name="referral", null =True, blank = True)
	name = models.CharField(max_length=200,default="FRESHMAN")
	ref_id = models.CharField(max_length=200,default="DEF_ID")
	ip_address = models.CharField(max_length=200,default="NULL_IP")

	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updatetime = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):  #names the individual instance ex self.email
		return self.email

	class Meta:
		unique_together = ['email', 'ref_id']

# class JoinFriends(models.Model):
# 	email = models.OneToOneField(Join, related_name="sharer")
# 	friends = models.ManyToManyField(Join, related_name="Friend", null =True, blank = True)

	# def __unicode__(self):  #names the individual instance ex self.email
		# print "firnds are", self.friends.all()
		
		# return "join instance is "+self.email