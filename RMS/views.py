from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from RMS.models import Add_Subjects , Assign_Subjects, Add_Students, Counter, Assign_Rollno_to_Students
from django.utils import timezone
# Create your views here.

def loginuser(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
       
        else:
            messages.error(request,"Please check your username or password!")
            # messages.error(request," Or you can try again later...")
            return redirect('loginuser')

    return render(request, 'loginuser.html')

def index(request):
    return render(request, 'home.html')

def logoutuser(request):
    logout(request)
    messages.success(request, "You were Logged out! Please Log in again")        
    return redirect('loginuser')

def add_subjects(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        subject_code = request.POST.get('subject_code')
        subject_code=subject_code.upper()
        date_and_time = timezone.now()
        record_of_subjects = Add_Subjects.objects.all()
                
        count=0
        for x in record_of_subjects:
            if subject_code == x.subject_code:
                # print(f'subjec code from template :- {subject_code} subjct code from databse: {x.subject_code}')
                count=1
                break
                
        if count==0:
            subjects_info=Add_Subjects(subject_name=subject_name.upper(),subject_code=subject_code.upper(), dateandtime = date_and_time)
            subjects_info.save()
            messages.success(request,f"Your subject {subject_code} has been successfully added")
        elif count==1 and count!=0: 
            messages.error(request,"This subject already exists!")
            return redirect('add_subjects')
        
        else:
            messages.error(request,"Please check your input")
            return redirect('add_subjects')

    return render(request, 'add_subjects.html')


def view_subjects_list(request):
    record_of_subjects = Add_Subjects.objects.all()
    records = {
        'record_of_subjects' : record_of_subjects
    }


    return render(request,"view_subjects_list.html",records)

def delete(request, id):
    Add_Subjects.objects.get(id=id).delete()        # command to delete record
    messages.success(request, "Record deleted successfuly.")
    return redirect("view_subjects_list")

def update(request,id):
    result=Add_Subjects.objects.get(id=id)
    
    if request.method == "POST":
        result.subject_name=request.POST.get('subject_name')
        result.subject_code=request.POST.get('subject_code')
        result.date_and_time = timezone.now()
        # info=Info(name=name.upper(),subject=subject.capitalize(),email=email,msg=msg.capitalize(),dateandtime = date_and_time)
        result.save()
        messages.success(request, "Record updated successfuly.")
        return redirect("view_subjects_list")

        # return render(request, "Info_table.html", records)
    
    return render(request, "update_info.html", {'result':result})

def assign_subjects(request):
    record_of_subjects = Add_Subjects.objects.all()
    records = {
        'record_of_subjects' : record_of_subjects
        # 'duplicate_subject_name' : subject_name
    }

    if request.method == "POST":
        class_number = request.POST.get('class_number')
        if class_number == 0 or class_number == "0":
            messages.error(request,"Please select the class!")
            # pass
            return redirect('assign_subjects')
        
        else:
            pass
        class_name = request.POST.get('class_name')
        if class_name == 0 or class_name == "0":
            messages.error(request,"Please select the stream!")
            # pass
            return redirect('assign_subjects')
        
        else:
            pass
        class_name = class_name.upper()
        subject_type = request.POST.get('subject_type')
        subject_code = request.POST.get('subject_code')
        if subject_code == 0 or subject_code == "0":
            messages.error(request,"Please select a Subject Code!")
            # pass
            return redirect('assign_subjects')
        
        else:
            pass
            
        subject_name = request.POST.get('subject_name')
        if subject_name == 0 or subject_name == "0":
            messages.error(request,"Please select a Subject Name!")
            # pass
            return redirect('assign_subjects')
        
        else:
            pass
            
        subject_code = subject_code.upper()
        date_and_time = timezone.now()

        record_of_assigned_subjects = Assign_Subjects.objects.all()

        count = 0
        for x in record_of_assigned_subjects:
            if class_name == x.class_name and subject_name == x.subject_name and subject_code == x.subject_code  :
            # if class_name == x.class_name :
                    count=1
                    print('already existsss')
                    break
        if count == 0:
                    assigned_subjects_info=Assign_Subjects(class_number=class_number, class_name = class_name,subject_type=subject_type.upper(), subject_code=subject_code,subject_name = subject_name.upper(), dateandtime = date_and_time)
                    assigned_subjects_info.save()
                    messages.success(request,f"Your subject {subject_code} has been successfully added as {subject_type}")

        else:
            messages.error(request,"Error! Please try again later")
            return redirect('assign_subjects')

        # for x in record_of_assigned_subjects:
        #     if class_name :
        #         if subject_code == x.subject_code:
        #             count=1
        #             break
        
        #         if count == 0:
        #             assigned_subjects_info=Assign_Subjects(class_number=class_number, class_name = class_name.upper(),subject_type=subject_type.upper(), subject_code=subject_code,subject_name = subject_name.upper(), dateandtime = date_and_time)
        #             assigned_subjects_info.save()
        #             messages.success(request,f"Your subject {subject_code} has been successfully added as {subject_type}")

        #         elif count!=0 and count >=1:
        #             messages.error(request, "This subject already exists!")
        #             return redirect('assign_subjects')

        #         else:
        #             messages.error(request,"Error! Please try again later")
        #             return redirect('assigned_subjects')
                
        #     elif class_name == 'non-medical' and 'medical' :
        #         if subject_code == x.subject_code:
        #             assigned_subjects_info=Assign_Subjects(class_number=class_number, class_name = class_name.upper(),subject_type=subject_type.upper(), subject_code=subject_code,subject_name = subject_name.upper(), dateandtime = date_and_time)
        #             assigned_subjects_info.save()
        #             messages.success(request,f"Your subject {subject_code} has been successfully added as {subject_type}")

        #         else:
        #             messages.error(request,"An unknown error occured!")
    return render(request, 'assign_subjects.html',records)

def view_assigned_subjects_list(request):
    record_of_assigned_subjects = Assign_Subjects.objects.all()
    assigned_subjects_list = {
        'records' : record_of_assigned_subjects
    }
    return render(request,"view_assigned_subjects_list.html",assigned_subjects_list)
    
def delete_assigned_subjects(request,id):
    Assign_Subjects.objects.get(id=id).delete()        # command to delete record
    messages.success(request, "Record deleted successfuly.")
    return redirect("view_assigned_subjects_list")

def update_assigned_subjects(request,id):
    result=Assign_Subjects.objects.get(id=id)
    
    if request.method == "POST":
        result.class_number = request.POST.get('class_number')
        result.class_name = request.POST.get('class_name')
        result.subject_type = request.POST.get('subject_type')
        result.subject_name=request.POST.get('subject_name')
        result.subject_code=request.POST.get('subject_code')
        result.date_and_time = timezone.now()
        # info=Info(name=name.upper(),subject=subject.capitalize(),email=email,msg=msg.capitalize(),dateandtime = date_and_time)
        result.save()
        messages.success(request, "Record updated successfuly.")
        return redirect("view_assigned_subjects_list")

        # return render(request, "Info_table.html", records)
    
    return render(request, "update_assigned_subjects.html", {'result':result})

def add_students(request):
    # students_id = Add_Students.objects.get(id=id)
    if request.method == "POST":
        class_number = request.POST.get('class_number')
        class_name = request.POST.get('class_name')
        class_name =class_name.upper()
        gender = request.POST.get('gender')
        gender = gender.upper()
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')

        # student_name = first_name + middle_name + last_name
        student_full_name = f"{first_name} {middle_name} {last_name}"

        student_full_name = student_full_name.upper()

        father_name = request.POST.get('father_name')
        father_name = father_name.upper()
        mother_name = request.POST.get('mother_name')
        mother_name = mother_name.upper()
        guardian_name = request.POST.get('guardian_name')
        guardian_name = guardian_name.upper()
        nationality = request.POST.get('nationality')
        nationality = nationality.upper()
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        if religion == 0 or religion =='0':
             messages.error(request,"Please select a religion")
             return redirect('add_students')
        
        else: pass

        religion= religion.upper()
        category = request.POST.get('category')
        if category == 0 or category =='0':
             messages.error(request,"Please select a category")
             return redirect('add_students')
        
        else: pass

        category= category.upper()
        blood_group = request.POST.get('blood_group')
        if blood_group == 0 or blood_group =='0':
             messages.error(request,"Please select a blood_group")
             return redirect('add_students')
        
        else: pass

        blood_group= blood_group.upper()
        aadhaar_no1 = request.POST.get('aadhaar_no1')
        aadhaar_no2 = request.POST.get('aadhaar_no2')
        aadhaar_no3 = request.POST.get('aadhaar_no3')

        aadhaar_number = f"{aadhaar_no1}{aadhaar_no2}{aadhaar_no3}"

        home_no = request.POST.get('home_no')
        building_name = request.POST.get('building_name')
        building_name = building_name.upper()
        area_name = request.POST.get('area_name')
        area_name = area_name.upper()
        district = request.POST.get('district')
        district = district.upper()
        state_or_ut = request.POST.get('state_or_ut')
        if state_or_ut == 0 or state_or_ut =='0':
             messages.error(request,"Please select a State/UT")
             return redirect('add_students')
        
        else: pass

        state_or_ut= state_or_ut.upper()
        pin_code = request.POST.get('pin_code')
        country = request.POST.get('country')
        if country == 0 or country =='0':
             messages.error(request,"Please select a country")
             return redirect('add_students')
        
        else: pass

        country= country.upper()

        full_address = f"{home_no} {building_name} {area_name} {district} {state_or_ut} {pin_code} {country}"

        father_phone_code = request.POST.get('father_phone_code')
        if father_phone_code == 0 or father_phone_code =='0':
             messages.error(request,"Please select a Phone code for Father's Phone number")
             return redirect('add_students')
        
        else: pass
        father_phone_no = request.POST.get('father_phone_no')

        father_phone_number = f"{father_phone_code} {father_phone_no}"

        mother_phone_code = request.POST.get('mother_phone_code')
        if mother_phone_code == 0 or mother_phone_code =='0':
             messages.error(request,"Please select a Phone code for Mother's Phone number")
             return redirect('add_students')
        
        else: pass
        mother_phone_no = request.POST.get('mother_phone_no')

        mother_phone_number = f"{mother_phone_code} {mother_phone_no}"

        guardian_phone_code = request.POST.get('guardian_phone_code')
        if guardian_phone_code == 0 or guardian_phone_code =='0':
             messages.error(request,"Please select a Phone code for Guardian's Phone number")
             return redirect('add_students')
        
        else: pass
        guardian_phone_no = request.POST.get('guardian_phone_no')

        guardian_phone_number = f"{guardian_phone_code} {guardian_phone_no}"

        father_email = request.POST.get('father_email')
        mother_email = request.POST.get('mother_email')
        guardian_email = request.POST.get('guardian_email')
        date_and_time = timezone.now()
        

        record_of_registered_students = Add_Students.objects.all()

        count = 0
        for x in record_of_registered_students:
            if class_name == x.class_name and father_phone_number == x.father_phone_number and mother_phone_number == x.mother_phone_number and guardian_phone_number == x.guardian_phone_number:
            # if class_name == x.class_name :
                    count=1
                    print('Already exists!')
                    break
        if count == 0:
                    registered_students_info=Add_Students(class_number=class_number, class_name = class_name,gender = gender, student_full_name = student_full_name, father_name = father_name , mother_name = mother_name, guardian_name = guardian_name, nationality = nationality, date_of_birth = date_of_birth, religion = religion, category = category, blood_group = blood_group, aadhaar_number = aadhaar_number, full_address = full_address, father_phone_number = father_phone_number, mother_phone_number = mother_phone_number, guardian_phone_number = guardian_phone_number, father_email = father_email, mother_email = mother_email, guardian_email = guardian_email, dateandtime = date_and_time)
                    registered_students_info.save()
                    messages.success(request,f"Student {student_full_name} has been registered successfully.")

        else:
            messages.error(request,"Error! Please try again later")
            return redirect('add_students')


        # roll_number = students_id

    

    return render(request,"add_student.html")

def assign_roll_number_to_students(request):

    record_of_class11=Add_Students.objects.filter(class_number='11')
    record_of_class12=Add_Students.objects.filter(class_number='12')
    
    registered_students = Add_Students.objects.all()
    counter = Counter.objects.all()
    ordered_records = registered_students.order_by('student_full_name')

    roll_number_list = Assign_Rollno_to_Students.objects.all()

    for all_records in ordered_records:

        # class_number = all_records.class_number
        # class_name = all_records.class_name
        gender = all_records.gender
        student_full_name = all_records.student_full_name
        father_name = all_records.father_name
        guardian_name = all_records.guardian_name
        date_of_birth = all_records.date_of_birth
        aadhaar_number = all_records.aadhaar_number
        father_phone_number = all_records.father_phone_number
        date_and_time = timezone.now()

    
    for c in counter:
         count=c.count

    if request.method == "POST":
        class_name = request.POST.get('class_name')
        class_name = class_name.upper()
        class_number = request.POST.get('class_number')

        print('hello')

        if class_number == '11' or class_number == 11:
            print('hello3')
            for r in record_of_class11:
                if class_name == 'HUMANITIES':
                    if class_name == r.class_name:
                        roll_number = f"{250}{11}{count}"
                        count+=1

                    print('hello1')

            count_verify = 0    

            for x in roll_number_list:

                if x.roll_number == roll_number:
                         
                    count_verify = 1
                    messages.error(request,"Already Registered!")
                    break
                    
            if count_verify == 0 :

                assign_rno = Assign_Rollno_to_Students(class_number = class_number,class_name = class_name, roll_number = roll_number,  gender=gender,student_full_name = student_full_name, father_name = father_name, guardian_name = guardian_name, date_of_birth = date_of_birth, aadhaar_number = aadhaar_number, father_phone_number = father_phone_number, dateandtime = date_and_time)

                assign_rno.save()

                print('hello2')
                messages.success(request,f"Roll Numbers are assigned to stream-class {class_name}{class_number}")


    
    

    # for r in ordered_records:
    #     # print(f'{r.student_full_name} and {r.class_name} and {r.class_number}')
    #     if r.class_name == 'MEDICAL':
    #           ccode=1
    #     elif r.class_name == 'NON-MEDICAL':
    #           ccode=2
    #     elif r.class_name == 'COMMERCE':
    #           ccode=3
    #     else:
    #           ccode=4

    #     roll_number=f'{r.class_number}{ccode}{count}'
    #     count+=1




    # if request.method == "POST":
    #     stream_and_class = request.POST.get('stream_and_class')
    # for y in range(0,record_of_registered_students):

    #     for x in record_of_registered_students:
    #         if stream_and_class =="011" :
    #             stream_and_class = 'HUMANITIES'

    #             if stream_and_class == x.class_name:
    #                 roll_number = f"{250}{11}{y}"

    #                 roll_number_list = Add_Students(roll_number=roll_number)
    #                 roll_number_list.save()
    #                 messages.success(request,f"Roll Numbers are assigned to {stream_and_class}")

    # return render(request,'assign_roll_number_to_students.html', {'ordered_records':ordered_records})
    return render(request,'assign_roll_number_to_students.html')