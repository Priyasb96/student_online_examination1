from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    branch = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.roll_number})"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Invigilator(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.employee_id})"


class Exam(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Midterm", "Final"
    date = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    invigilator = models.ForeignKey(Invigilator, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject.name}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    total_marks = models.FloatField()

    def __str__(self):
        return f"{self.student.name} - {self.exam.name}"

    def percentage(self):
        return (self.marks_obtained / self.total_marks) * 100