from django.db import models

class SourceCodeCategory(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'source categories'

class SourceCode(models.Model):
	source_title = models.CharField(max_length=255)
	#source_file = models.CharField(max_length=500, null=True, blank=True)
	deployment_url = models.CharField(max_length=500, null=True, blank=True)
	description = models.TextField()
	source_code = models.TextField(null=True, blank=True)
	language = models.CharField(max_length=100)
	categories = models.ManyToManyField(SourceCodeCategory)

	def __unicode__(self):
		return self.source_title

