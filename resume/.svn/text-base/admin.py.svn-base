from django.contrib import admin
from resume.models import *

class MainSectionInline(admin.StackedInline):
	model = MainSection
	extra = 10

class ResumeAdmin(admin.ModelAdmin):
	inlines = [MainSectionInline]

class ListItemInline(admin.StackedInline):
	model = ListItem
	extra = 10

class ListContentAdmin(admin.ModelAdmin):
	inlines = [ListItemInline]

class TableAlphaListItemInline(admin.StackedInline):
	model = TableAlphaListItem
	extra = 20

class TableRowInline(admin.StackedInline):
	model = TableRow
	extra = 6

class TableContentAdmin(admin.ModelAdmin):
	inlines = [TableRowInline]

class TableRowAdmin(admin.ModelAdmin):
	inlines = [TableAlphaListItemInline]

admin.site.register(Resume, ResumeAdmin)
admin.site.register(TextContent)
admin.site.register(ListContent, ListContentAdmin)
admin.site.register(TableContent, TableContentAdmin)
admin.site.register(TableRow, TableRowAdmin)
admin.site.register(ChronologicalEntry)
