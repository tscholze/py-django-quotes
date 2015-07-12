from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core import serializers

from .models import Quote

class IndexView(generic.ListView):
	template_name = "quotes/index.html"
	context_object_name = 'latest_quote_list'
	def get_queryset(self):
		"""Return the ten latest quotes"""
		return Quote.objects.order_by('-pub_date')[:10]

def quotes_as_json(self):
	data = serializers.serialize("json", Quote.objects.order_by('-pub_date')[:10])
	return HttpResponse(data, content_type='application/json')	 
