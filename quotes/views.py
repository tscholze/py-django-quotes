from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Quote

class IndexView(generic.ListView):
	template_name = "quotes/index.html"
	context_object_name = 'latest_quote_list'
	def get_queryset(self):
		"""Return the ten latest quotes"""
		return Quote.objects.order_by('-pub_date')[:10] 