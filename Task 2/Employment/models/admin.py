from django.contrib import admin
from .models import Job, Employer

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'validity_date', 'category', 'salary', 'working_hours')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(employer__user=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.employer.user != request.user:
            return False
        return True

admin.site.register(Job, JobAdmin)
admin.site.register(Employer)