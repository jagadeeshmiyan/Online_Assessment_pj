from django.contrib import admin

# Register your models here.
from .models import Assessment

admin.site.register(Assessment)

# @admin.register(Assessment)
# class AssessmentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'assessment_type', 'instructions', 'time_limit', 'attempts_allowed')
