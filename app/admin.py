from django.contrib import admin
from app.models import Author, JobPost, Location, Skill


class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'salary', 'date',)
    list_filter = ('date', 'salary', 'expiry',)
    search_fields = ('title', 'description',)
    search_help_text = "Write in your query and hit enter"
    fields = (('title', 'description'), 'salary', 'expiry',)
    exclude = ('slug',)
    fieldsets = (
        ('Basic information', {
            # 'classes': ('collapse', 'wide',),
            'fields': ('title', 'description',)
        }),
        ('More information', {
            'classes': ('collapse', 'wide',),
            'fields': (('expiry', 'salary'), 'slug',)
        }),
    )


# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)
