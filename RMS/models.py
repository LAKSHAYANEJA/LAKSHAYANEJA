from django.db import models
from django.utils import timezone

# Create your models here.
class Add_Subjects(models.Model):
    subject_name=models.TextField(max_length=(60))
    subject_code=models.TextField(max_length=(20))
    dateandtime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject_code
    
class Assign_Subjects(models.Model):
    class_number = models.IntegerField()
    class_name = models.TextField(max_length=(20))
    subject_type = models.TextField(max_length=(20))
    subject_name = models.TextField(max_length=(60))
    subject_code=models.TextField(max_length=(20))
    dateandtime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.subject_code

class Add_Students(models.Model):
    class_number = models.IntegerField()
    class_name = models.TextField(max_length=(20))
    roll_number = models.TextField(max_length=(10))
    gender = models.TextField(max_length=(12))
    # first_name = models.TextField(max_length=(50))
    # middle_name = models.TextField(max_length=(50))
    # last_name = models.TextField(max_length=(50))
    student_full_name = models.TextField(max_length=(200))
    father_name = models.TextField(max_length=(60))
    mother_name = models.TextField(max_length=(60))
    guardian_name = models.TextField(max_length=(60))
    nationality = models.TextField(max_length=(20))
    date_of_birth = models.DateField()
    religion = models.TextField(max_length=(10))
    category = models.TextField(max_length=(15))
    blood_group = models.TextField(max_length=(5))
    aadhaar_number = models.TextField(max_length=(12))
    full_address = models.TextField(max_length=(250))
    father_phone_number = models.TextField(max_length=(15))
    mother_phone_number = models.TextField(max_length=(15))
    guardian_phone_number = models.TextField(max_length=(15))
    father_email = models.EmailField(max_length=(40))
    mother_email = models.EmailField(max_length=(40))
    guardian_email = models.EmailField(max_length=(40))
    dateandtime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.aadhaar_number
    
class Assign_Rollno_to_Students(models.Model):
    class_number = models.IntegerField()
    class_name = models.TextField(max_length=(20))
    roll_number = models.TextField(max_length=(10))
    gender = models.TextField(max_length=(12))
    student_full_name = models.TextField(max_length=(200))
    father_name = models.TextField(max_length=(60))
    guardian_name = models.TextField(max_length=(60))
    date_of_birth = models.DateField()
    aadhaar_number = models.TextField(max_length=(12))
    father_phone_number = models.TextField(max_length=(15))
    dateandtime = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.roll_number
    
class Counter(models.Model):
    count = models.IntegerField()
    