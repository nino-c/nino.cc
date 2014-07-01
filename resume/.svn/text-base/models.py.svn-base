from django.db import models

class Resume(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=100)
	email = models.EmailField()
	address = models.TextField()
	phone = models.CharField(max_length=20)
	summary = models.TextField()

	def __unicode__(self):
		return self.title + ' (' + self.subtitle + ')'

class MainSection(models.Model):
	resume = models.ForeignKey(Resume)
	heading = models.CharField(max_length=100)
	order = models.FloatField()

	def __unicode__(self):
		return self.heading

class TextContent(models.Model):
	parent_section = models.ForeignKey(MainSection)
	order = models.FloatField()
	text = models.TextField()

	def __unicode__(self):
		return self.text[:10]

class ListContent(models.Model):
	parent_section = models.ForeignKey(MainSection)
	order = models.FloatField()

	def __unicode__(self):
		return self.parent_section.heading

class ListItem(models.Model):
	parent_list = models.ForeignKey(ListContent)
	order = models.FloatField()
	text = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.text[:20]

	class Meta:
		ordering = ['order']

class TableContent(models.Model):
	parent_section = models.ForeignKey(MainSection)
	order = models.FloatField()

	class Meta:
		ordering = ['order']

class TableRow(models.Model):
	parent_table = models.ForeignKey(TableContent)
	order = models.FloatField()
	label = models.CharField(max_length=300)

	def __unicode__(self):
		return self.label

	class Meta:
		ordering = ['order']

class TableAlphaListItem(models.Model):
	parent_table_row = models.ForeignKey(TableRow)
	value = models.CharField(max_length=300)

	def __unicode__(self):
		return self.value

	class Meta:
		ordering = ['value']

class ChronologicalEntry(models.Model):
	parent_section = models.ForeignKey(MainSection)
	heading = models.CharField(max_length=300)
	subheading = models.CharField(max_length=300)
	begin_year = models.IntegerField()
	end_year = models.IntegerField(blank=True, null=True)
	text = models.TextField()

	def __unicode__(self):
		return self.heading

	class Meta:
		ordering = ['id']

