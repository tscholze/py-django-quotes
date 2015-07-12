from django.db import models

class Quote(models.Model):
	"""Represents a quote that is voteable"""
	quote_text = models.CharField(max_length=300)
	author_name = models.CharField(max_length=25, default='N/A')
	votes = models.IntegerField(default = 0)
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	
	def __str__(self):
		return self.quote_text
