from django.shortcuts import render
import datetime,re,json,requests,random,time
from random import randint
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from .models import *
import traceback
from validate_email import validate_email
import glob
import face_recognition
import numpy as np
import JuVeNiLe
import smtplib
import os
from logisticRegression.predict import getPrediction ;
from JuVeNiLe.settings import BASE_DIR

import os


def logoutView(request):
    if not True:
        return HttpResponse(
            json.dumps({"redirectConstant": 'Login', "validation": 'Invalid login details', "status": False}),
            content_type="application/json")
    else:
        logout(request)
        return HttpResponse(
            json.dumps({"redirectConstant": "Login", "validation": "logged out successfully", "status": True}),
            content_type="application/json")

def loginView(request):
    jsonObj = json.loads(request.body.decode("utf-8"))
    print
    jsonObj
    username = jsonObj['username']
    password = jsonObj['password']

    if not username or not password:
        return HttpResponse(json.dumps({"validation": 'Fill all details', "status": False}),
                            content_type="application/json")


    user = authenticate(username=username, password=password)

    if user is not None:

        if user.is_active:

            login(request, user)

            u = {}
            u['userId'] = user.id
            u['userName'] = user.username

            return HttpResponse(json.dumps(
                {"redirectConstant": "Home", "validation": "logged In successfully", "data": u, "status": True}),
                                content_type="application/json")

        else:
            print("here")
            return HttpResponse(json.dumps({"validation": "Invalid login details..!!", "status": False}),
                                content_type="application/json")
    else:
        print("qwertyuiop")
        return HttpResponse(json.dumps({"validation": "Invalid login details..!!", "status": False}),
                            content_type="application/json")


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

 # send OTP mail
def senOtpMail(mailId):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("juvenilebe@gmail.com", "hesoyamfullclip")

    otpCode = random_with_N_digits(4)

    PendingData = PendingUsers.objects.filter(userName= mailId)

    if PendingData:
        PendingData[0].delete()

    pu = PendingUsers()
    pu.userName = mailId
    pu.otpCode = otpCode
    pu.save()

    # message to be sent
    message = "Here is your OTP " + str(otpCode) + " . Please verify youself by using this on website"

    # sending the mail
    s.sendmail("juvenilebe@gmail.com",mailId,  message)

    # terminating the session
    s.quit()



def verifyOtp(request):
    try:

        jsonObj = json.loads(request.body.decode("utf-8"))
        print(jsonObj)
        otp = jsonObj.get('otp')
        username = jsonObj.get('username')
        pendingUserData = PendingUsers.objects.filter(userName= username, otpCode = otp) ;
        if not pendingUserData:

            return HttpResponse(
                json.dumps({"validation": "OTP verification Failed", "status": False}),
                content_type="application/json")


        pendingUserData[0].delete()
        currentUser = User.objects.get(username= username) ;
        currentUser.is_active = True
        currentUser.save()
        loginView(request)
        return HttpResponse(
            json.dumps({"validation": "OTP verified successfully", "status": True}),
            content_type="application/json")
    except:
        traceback.print_exc()
        return HttpResponse(
            json.dumps({"validation": "Error in verifying OTP", "status": False}),
            content_type="application/json")


def resendOtp(request):
    try:
        jsonObj = json.loads(request.body.decode("utf-8"))
        username = jsonObj.get('username')
        senOtpMail(username)
        return HttpResponse(
            json.dumps({"validation": "OTP sent again", "status": True}),
            content_type="application/json")
    except:
        traceback.print_exc()
        return HttpResponse(
            json.dumps({"validation": "Error while resending OTP", "status": False}),
            content_type="application/json")



def register_user(request):
    print(request.body)
    jsonObj = json.loads(request.body.decode("utf-8"))
    username = jsonObj.get('username')

    try:
        userData = User.objects.get(username=username)

        if not userData.is_active:
            userData.delete()
            u = User()
            if validate_email(username):

                u.username = username
                u.set_password(str(jsonObj.get('password')))
                u.is_active = False
                u.save()
                senOtpMail(username);
                userObj = {}
                userObj['userId'] = u.id
                userObj['userName'] = u.username

                return HttpResponse(
                    json.dumps({"validation": 'User register successfully', "user": userObj, "status": True,
                                "redirectConstant": 'User Profile'}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"validation": 'Invalid EmailID', "status": False}),
                                    content_type="application/json")

        else:
            return HttpResponse(
                json.dumps({"validation": 'Username already registered in the system', "status": False}),
                content_type="application/json")



    except:
        u = User()
        if validate_email(username):

            u.username = username
            u.set_password(str(jsonObj.get('password')))
            u.is_active = False
            u.save()
            senOtpMail(username);
            userObj = {}
            userObj['userId'] = u.id
            userObj['userName'] = u.username


            return HttpResponse(json.dumps({"validation": 'User register successfully', "user": userObj, "status": True,
                                            "redirectConstant": 'User Profile'}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"validation": 'Invalid EmailID', "status": False}),
                                content_type="application/json")




# scan police records
def scanPoliceRecord(myImage):
    record = []
    pic = face_recognition.load_image_file(JuVeNiLe.settings.BASE_DIR + myImage.url)
    for filepath in glob.iglob('Media/criminal_records/encoding/*.txt'):
        encoding1 = np.loadtxt(filepath, delimiter=",")
        encoding2 = face_recognition.face_encodings(pic)[0]
        if face_recognition.compare_faces([encoding1],encoding2)[0]:
            try:
                pr = PoliceCriminalRecord.objects.get(id=int(os.path.splitext(os.path.basename(filepath))[0]))
                record.append({
                "Name" : pr.name ,
                "Age":pr.age ,
                "School Admission":pr.schoolAdmission ,
                "Gender" : pr.gender.name,
                "School Name" :pr.schoolName ,
                "Location Of Child":pr.locationOfChild ,
                "Parents Employment" : pr.parentsEmployment ,
                "Parents Location Of Work" : pr.parentsLocationOfWork ,
                "Income" : pr.income ,
                "Criminal Record Description" : pr.criminalRecordDescription ,
                "Medical Record" :pr.medicalRecord ,
                "Medical Record Description" : pr.medicalRecordDescription ,
                "Image Of Child" : pr.imageOfChild.url ,
                });
            except:
                pass


    return record



# scan lost and found
def scanLostAndFound(myImage):

    record = []
    pic = face_recognition.load_image_file(JuVeNiLe.settings.BASE_DIR + myImage.url)
    for filepath in glob.iglob('Media/lost_and_found_records/encoding/*.txt'):
        encoding1 = np.loadtxt(filepath, delimiter=",")
        encoding2 = face_recognition.face_encodings(pic)[0]
        if face_recognition.compare_faces([encoding1], encoding2)[0]:
            try:
                pr = LostAndFoundRecords.objects.get(id=int(os.path.splitext(os.path.basename(filepath))[0]))
                record.append({
                "Name" : pr.name ,
                "Age":pr.age ,
                "School Admission":pr.schoolAdmission ,
                "School Name" :pr.schoolName ,
                "Gender": pr.gender.name,
                "Location Of Child Lost":pr.locationOfChildLost ,
                "Gaurdian Name": pr.gaurdianName,
                "Location Of Contact": pr.locationToContact,
                "Gaurdian Contact Number": pr.gaurdianContactNumber,
                "Image Of Child" : pr.imageOfChild.url ,
                });
            except:
                pass

    return record



# ************************ Get Logistic Regression Prediction  **************************


def getLogisticPrediction(request):
    try:
        # This is suppose to be a array e.g. [0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0]
        data = json.loads(request.body.decode('utf-8'))
        print(data["data"])
        print(getPrediction(data["data"]))
        return HttpResponse(json.dumps({
             "prediction":getPrediction(data["data"]).tolist() ,
                                        "status": True}),
                            content_type="application/json")
    except:
        traceback.print_exc()

        return HttpResponse(json.dumps({"validation": 'Error In making prediction', "status": False}),
                            content_type="application/json")




# ****************************  End of logistic regression prediction  *************************




#**************************** Mail cron job *******************************************

def send_mail_notification():
    try:
        medicalCheckupNotDone = MedicalCheckup.objects.filter(medicalCheckupStatus=False)
        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login("juvenilebe@gmail.com", "hesoyamfullclip")
        for obj in medicalCheckupNotDone:
            message = "It appear to us that you have not done medical checkup fo the child name" + str((
                                                                                                           RegisteredChildren.objects.get(
                                                                                                               id=obj.child)).name) + ". please do it as soon as possible or if you have done it please share the reports with us on our email"
            s.sendmail("juvenilebe@gmail.com", (OrphanageNgo.objects.get(id=obj.assignedTo)).email, message)

            # terminating the session
        s.quit()
    except:

        file_path = os.path.join(BASE_DIR, 'log.txt')
        f = open(file_path, "a")
        f.write(str(traceback.print_exc()))




#******************************* End mail cron job **************************************


def register_child(request):
    try:

        print(request.POST['age'])
        print(request.FILES)
        data = request.POST ;
        files = request.FILES
        rc = RegisteredChildren()

        print(datetime.datetime.strptime(data["dob"],"%Y-%m-%d"))

        rc.user = request.user ;

        rc.registration_date = datetime.datetime.today();

        rc.name = data["name"] if "name" in data else None

        rc.age =  data["age"] if "age" in data else None

        rc.dob =  data["dob"] if "dob" in data else None

        rc.category =  ChildCategory.objects.get(id=data["category"]) if "category" in data else None;

        rc.gender = ChildGender.objects.get(id=data["gender"]) if "gender" in data else None;

        if "school" in data:
            rc.schoolAdmission = True if data["school"]=="t" else False;

        if "parentsWork" in data:
            rc.parentsEmployment = True if data["parentsWork"] == "t" else False;

        rc.schoolName = data["schoolDes"] if "schoolDes" in data else None;

        rc.locationOfChild = data["location"] if "location" in data else None;

        rc.childFoundTime = data["time"] if "time" in data else None;



        rc.parentsLocationOfWork = data["parentsWorkLocation"] if "parentsWorkLocation" in data else None ;

        rc.income = data["parentsIncome"] if "parentsIncome" in data else None ;

        rc.imageOfChild = files["childPhoto"] if "childPhoto" in files else None;

        rc.birthMark = files["birthMark"] if "birthMark" in files else None

        rc.save()

        while not os.path.exists(JuVeNiLe.settings.BASE_DIR+rc.imageOfChild.url):
            time.sleep(1)

        if os.path.isfile(JuVeNiLe.settings.BASE_DIR+rc.imageOfChild.url):
            pass
        else:
            raise ValueError("isn't a file!")

        return HttpResponse(json.dumps({"validation": 'Child register successfully' ,
                                        "policeRecord":scanPoliceRecord(rc.imageOfChild) ,
                                       "lostRecord":scanLostAndFound(rc.imageOfChild),
                                        "status": True}),
                            content_type="application/json")
    except:
        traceback.print_exc()
        return HttpResponse(json.dumps({"validation": 'Error In registering child', "status": False}),
                            content_type="application/json")





