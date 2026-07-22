
import random
from django.db.models import Sum,Q,F,Avg,Max,Min
from faker import Faker
from .models import *
fake = Faker()

def create_marks():
    
        student_obj = Student.objects.all()
        for student in student_obj:
            subject_obj = Subject.objects.all()
            for s in subject_obj:
                SubjectMarks.objects.create(
                    student = student,
                    subject = s,
                    marks = random.randint(40,100)
                )
    
def seed_db(n=10):
    try:
        for i in range(0,n):
            department_obs = Department.objects.all()
            r_ind = random.randint(0,len(department_obs)-1)
            department = department_obs[r_ind]
            student_id = f'STU-0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(19,30)
            student_address = fake.address()
            
            s_i_o = StudentID.objects.create(student_id = student_id)
            s_o = Student.objects.create(
                
                department = department,
                student_id = s_i_o,
                student_name = student_name,
                student_age = student_age,
                student_email = student_email,
                student_address = student_address,
            )
    except Exception as e:
        print(e)
def generate_reportcard(s_id):
    rank = Student.objects.annotate(t_marks = Sum("studentss__marks")).order_by("-t_marks" , "-student_age")
    i=1
    rankk =1
    for r in rank:  
        ReportCard.objects.create(
            student = r,
            student_rank = i
        )
        i+=1

    