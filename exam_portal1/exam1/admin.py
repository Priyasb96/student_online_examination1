from django.contrib import admin
from .models import Student, Subject, Invigilator, Exam, Result


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email', 'branch', 'year')
    search_fields = ('name', 'roll_number', 'branch')
    list_filter = ('branch', 'year')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'semester')
    search_fields = ('name', 'code')
    list_filter = ('semester',)


@admin.register(Invigilator)
class InvigilatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'email')
    search_fields = ('name', 'employee_id')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'subject', 'invigilator')
    search_fields = ('name', 'subject_name', 'invigilator_name')
    list_filter = ('date', 'subject', 'invigilator')


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks_obtained', 'total_marks', 'percentage_display')
    search_fields = ('student_name', 'exam_name')
    list_filter = ('exam__name',)

    def percentage_display(self, obj):
        return f"{obj.percentage():.2f}%"
    percentage_display.short_description = 'Percentage'