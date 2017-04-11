from django.conf import settings
from django.db import models

from django_hosts.resolvers import reverse

from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

# Create your models here.
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShortenedURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(ShortenedURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs


	def refresh_shortcodes(self):
		qs = ShortenedURL.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_codes += 1
		return "New codes made: {i}".format(i=new_codes)


class ShortenedURL(models.Model):
	url = models.CharField(max_length = 220, validators=[validate_url, validate_dot_com])
	shortcode = models.CharField(max_length = SHORTCODE_MAX, unique=True, blank=True)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True,)
	active = models.BooleanField(default=True)

	objects = ShortenedURLManager()

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		if not "http://" in self.url:
			if not "https://" in self.url:
				self.url = "http://" + self.url
		super(ShortenedURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	def get_short_url(self):
		url_path = reverse("scode", kwargs={"slug": self.shortcode}, scheme="http", port="8000")
		return url_path