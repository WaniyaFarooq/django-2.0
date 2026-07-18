import random

from faker import Faker
from .models import *
fake = Faker()

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