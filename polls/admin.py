from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets= [
		('Date Information',{'fields':['pub_date'],'classes': ['collapse']}),
		(None,{'fields':['question']}),
		]
	inlines = [ChoiceInLine]
	list_display=('question','pub_date','is_recent')
	list_filter=['pub_date']
	search_fields = ['question']
 	date_hierarchy = 'pub_date'
	

admin.site.register(Poll,PollAdmin)

