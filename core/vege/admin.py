from django.contrib import admin

# Register your models here.
from .models import *
from django.db.models import Sum,Avg
admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(SubjectMarks)
admin.site.register(Subject)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']
    
admin.site.register(SubjectMarkAdmin)
class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks','date_of_reportcard_generation']
    def total_marks(self,obj):
        s_m = SubjectMarks
        return
admin.site.register(ReportCard,ReportCardAdmin)