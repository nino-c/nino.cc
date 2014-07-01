from django.db import models
from mezzanine.galleries.models import Gallery
from mezzanine.core.models import RichText
from mezzanine.pages.models import Page

class ProjectCategory(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'categories'

class Project(Gallery, Page):
	project_title = models.CharField(max_length=255)
	url = models.URLField(null=True, blank=True)
	categories = models.ManyToManyField(ProjectCategory)
	summary = models.TextField(null=True, blank=True)
	specs = models.TextField(null=True, blank=True)
	begin_date = models.IntegerField()
	end_date = models.IntegerField(null=True, blank=True)
	show_photos = models.BooleanField()

	def __unicode__(self):
		return self.title

	def get_main_photo(self):
		photo = self.gallery.images.all()[:1].get()
		return photo

	def get_gallery(self):
		return self.gallery
