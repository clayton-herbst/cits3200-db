from django.contrib import admin, auth
from django.contrib.auth.models import User, Group
from .models import funding_opportunity
from django.utils.html import format_html
# Register your models here.


#admin.site.register(Post)
#admin.site.register(funding_opportunity)
#admin.site.register(important_date)

admin.site.site_header = 'Funding Opportunities Database'

class important_dateInline(admin.TabularInline):
    model = important_date
    extra = 1

class FundingOpportunityAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Funding Opportunity',{'fields': ['name','description','link','herdc','limit_per_uni']}),
        ('Date Information', {'fields': ['closing_month']}),
        ('Amount and Duration', {'fields': ['max_amount','amount_estimated','max_duration','duration_type','duration_estimated']}),
        ('Tags', {'fields': ['ecr','travel','visiting','wir','phd','international','hms','ems','science','is_hidden' ]}),
    ]
	inlines = [important_dateInline]
	list_filter = ('closing_month', )
	list_display = ('name', 'closing_month','max_amount','max_duration')
	search_fields = ['description','name']

admin.site.register(funding_opportunity,FundingOpportunityAdmin)

class UserAdmin(admin.ModelAdmin):
	search_field = ('name')



admin.site.unregister(Group)