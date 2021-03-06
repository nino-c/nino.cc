import datetime
from django.db import models


class Composer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	birth = models.IntegerField(null=True, blank=True)
	death = models.IntegerField(null=True, blank=True)
	birthday = models.DateField(null=True, blank=True)
	deathday = models.DateField(null=True, blank=True)
	index_name = models.CharField(max_length=8, null=True, blank=True)

	def get_last_name(self):
		if '|' in self.last_name:
			return self.last_name.split('|')[0]
		else:
			return self.last_name

	def get_first_name(self):
		if '|' in self.first_name:
			return self.first_name.split('|')[0]
		else:
			return self.first_name

	def __unicode__(self):
		return self.get_last_name() + ', ' + self.get_first_name()

	class Meta:
		ordering = ['last_name', 'first_name']

class Tag(models.Model):
	name = models.CharField(max_length=80)

	def __unicode__(self):
		return self.name

class MusicalWork(models.Model):
	composer = models.ForeignKey(Composer)
	title = models.CharField(max_length=1000)
	key = models.CharField(max_length=20, null=True, blank=True)
	work_index = models.IntegerField(null=True, blank=True)
	work_index_num = models.IntegerField(null=True, blank=True)
	date_written = models.IntegerField(null=True, blank=True)
	tags = models.ManyToManyField(Tag)


	def __unicode__(self):
		return self.composer.get_last_name() + ': ' + self.get_full_title()

	def get_full_title(self):
		label = str(self.title)
		if self.key:
			label += ' in ' + str(self.key)
		if self.composer.index_name and self.work_index:
			label += ' ' + str(self.composer.index_name) + ' ' + str(self.work_index)
		if self.work_index_num:
			label += ' no. ' + str(self.work_index_num)
		return label

	class Meta:
		ordering = ['composer__last_name', 'title', 'work_index', 'work_index_num']

class Movement(models.Model):
	work = models.ForeignKey(MusicalWork)
	title = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['id']


class PressQuote(models.Model):
	publication = models.CharField(max_length=255)
	date = models.DateField(null=True, blank=True)
	quote = models.TextField()

	def __unicode__(self):
		return self.publication + ': ' + self.quote[:10] + '...'

#######################################################

class CD(models.Model):
	title = models.CharField(max_length=500)
	release_year = models.IntegerField()
	producer = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	image = models.CharField(max_length=255)

	def __unicode__(self):
		return self.title

class CDlink(models.Model):
	url = models.URLField()
	image = models.FileField(upload_to="/static/img/", null=True, blank=True)
	cd = models.ForeignKey(CD)
