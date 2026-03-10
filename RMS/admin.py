from django.contrib import admin
from RMS.models import Add_Subjects, Assign_Subjects, Add_Students, Counter, Assign_Rollno_to_Students

# Register your models here.
admin.site.register(Add_Subjects)
admin.site.register(Assign_Subjects)
admin.site.register(Add_Students)
admin.site.register(Counter)
admin.site.register(Assign_Rollno_to_Students)

class InfoAdmin(admin.ModelAdmin):
    readonly_fields = ('dateandtime',)
# Register your models here.
