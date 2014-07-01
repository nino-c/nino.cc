from django.db import models
from rep.models import MusicalWork
from django.forms import ModelForm, CheckboxSelectMultiple, CheckboxInput
from django.forms.extras.widgets import SelectDateWidget
from itertools import chain
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe


class ListCheckboxSelectMultiple(CheckboxSelectMultiple):
    def render(self, name, value, ulattrs=None, attrs=None, choices=()):
        if value is None: value = []
        has_id = attrs and 'id' in attrs
        final_attrs = self.build_attrs(attrs, name=name)
        #output = [u'<ul class="%s">' % ulattrs.get('class')]
        output = [u'<br />']
        # Normalize to strings
        str_values = set([force_unicode(v) for v in value])
        for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
            # If an ID attribute was given, add a numeric index as a suffix,
            # so that the checkboxes don't all have the same ID attribute.
            if has_id:
                final_attrs = dict(final_attrs, id='%s_%s' % (attrs['id'], i))
                label_for = u' for="%s"' % final_attrs['id']
            else:
                label_for = ''

            cb = CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
            option_value = force_unicode(option_value)
            rendered_cb = cb.render(name, option_value)
            option_label = conditional_escape(force_unicode(option_label))
            output.append(u'%s %s<br />' % (rendered_cb, option_label))
        #output.append(u'</ul>')
        return mark_safe(u'\n'.join(output))

class AudioSet(models.Model):
	set_name = models.CharField(max_length=256)

class AudioFile(models.Model):
	audioset = models.ForeignKey(AudioSet)
	file = models.FileField(upload_to='/static/audio')

class Concert(models.Model):
	date = models.DateField()
	date_approximate = models.BooleanField(default=False)
	venue = models.CharField(max_length=512)
	institution = models.CharField(max_length=512, null=True, blank=True)
	city = models.CharField(max_length=256)
	state = models.CharField(max_length=64, null=True, blank=True)
	country = models.CharField(max_length=64, null=True, blank=True, default='US')
	concert_subtitle = models.CharField(max_length=256, null=True, blank=True)
	concert_description = models.TextField(verbose_name='Other Information', null=True, blank=True)
	works = models.ManyToManyField('rep.MusicalWork', null=True, blank=True)
	audio = models.ManyToManyField(AudioSet, null=True, blank=True)
	show = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.date) + " " + self.venue + ", " + self.city

class ConcertForm(ModelForm):
	class Meta:
		model = Concert
		exclude = ('date_approximate', 'concert_subtitle',  'show', 'audio')
		widgets = {
			'date': SelectDateWidget(years=[
				'1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005',
				'2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', 
				'2014'
				]),
			'works': ListCheckboxSelectMultiple(),
		}

class ConcertSubmission(models.Model):
	concert = models.ForeignKey(Concert)
	pending = models.BooleanField(default=True)
	submitted_by = models.EmailField(verbose_name='Your email')
	date_submitted = models.DateTimeField(auto_now=True)
	remote_ip = models.IPAddressField()

	def __unicode__(self):
		return str(self.date_submitted)