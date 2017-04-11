from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import ShortenedURL

# Create your views here.
class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = SubmitUrlForm()
		context = {
			"title" : "Anything Philippines", 
			"form" : form
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title": "Anything Philippines",
			"form": form
		}

		template = "shortener/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")
			obj, created = ShortenedURL.objects.get_or_create(url=new_url)
			context = {
				"obj": obj,
				"created": created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		return render(request, template, context)


class URLRedirectView(View):
	def get(self, request, slug=None, *args, **kwargs):
		obj = get_object_or_404(ShortenedURL, shortcode=slug)

		#save item
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)

	def post(self, request, *args, **kwargs):
		return HttpResponse()