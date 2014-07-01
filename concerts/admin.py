from django.contrib import admin
from nested_inlines.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
from django.forms import CheckboxSelectMultiple
from django.utils.safestring import mark_safe
from concerts.models import *
from rep.models import *
from rep.admin import *

class MusicalWorkInline(admin.TabularInline):
	model = Concert.works.through
	extras = 5
	#widget = ListCheckboxSelectMultiple()
	#formfield_overrides = { models.ManyToManyField: {'widget': ListCheckboxSelectMultiple()}, }

class AudioSetInline(NestedTabularInline):
	model = Concert.audio.through
	extras = 5

class ConcertAdmin(admin.ModelAdmin):
	#inlines = [MusicalWorkInline]
	#widget = CheckboxSelectMultiple()
	formfield_overrides = { models.ManyToManyField: {'widget': ListCheckboxSelectMultiple()}, }
	

class AudioSetAdmin(admin.ModelAdmin):
	inlines = [AudioSetInline]

admin.site.register(Concert, ConcertAdmin)
admin.site.register(AudioSet)
admin.site.register(ConcertSubmission)
