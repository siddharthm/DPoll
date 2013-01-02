from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Poll(models.Model):

	def __unicode__(self):
		return self.question
	def is_recent(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days=5))
	is_recent.admin_order_field = 'pub_date'
	is_recent.boolean = True
	is_recent.short_description = 'Published recently?'
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date Published')
	
class Choice(models.Model):
	def __unicode__(self):
		return self.choice
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	
