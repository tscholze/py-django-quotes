from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core import serializers
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from .models import Quote

class IndexView(generic.ListView):
	template_name = "quotes/index.html"
	context_object_name = 'latest_quote_list'
	def get_queryset(self):
		"""Return the ten latest quotes"""
		return Quote.objects.order_by('-pub_date')[:10]
		
class DetailView(generic.DetailView):
	model = Quote
	template_name = "quotes/detail.html"

class LatestQuotesFeed(Feed):
	feed_type = Atom1Feed
	title = "-- Quotes --"
	link = "/sitenews/"
	description = "Do not forget unique spoken words"
	
	def items(self):
		return Quote.objects.order_by('-pub_date')[:10]
	
	def item_title(self, item):
		return item.quote_text

	def item_description(self, item):
		return item.author_name
		
	def item_link(self, item):
		return reverse('quotes:detail', args=(item.pk,))
	
def quotes_as_json(self):
	data = serializers.serialize("json", Quote.objects.order_by('-pub_date')[:10])
	return HttpResponse(data, content_type='application/json')	 
