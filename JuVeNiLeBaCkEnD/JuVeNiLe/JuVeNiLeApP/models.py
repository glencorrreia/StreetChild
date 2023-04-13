import os,re,json,requests
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import JuVeNiLe
import random
import face_recognition
import numpy as np
import face_recognition



def get_image_upload_dir(structure=[]):

	fileStructure = ""

	for data in structure:
		fileStructure += data + "/"

	if not os.path.isdir(JuVeNiLe.settings.BASE_DIR+'/Media/' + fileStructure): # will go in if statement, if required directory is exist.
		os.makedirs(JuVeNiLe.settings.BASE_DIR + '/Media/'+fileStructure)
	return fileStructure


# get unique id
def getId():
    myId = ""
    for x in range(10):
        myId = myId+str(random.randint(1,101))

# pendimg users table
class PendingUsers(models.Model):
    userName  = models.CharField(max_length=255,null=True, blank =True);
    otpCode = models.IntegerField(null=True, blank =True);

    def __str__(self):
        return str(self.userName)

    class Meta:
        verbose_name = 'List Of Pending Users'
        verbose_name_plural = 'List Of Pending Users'



#child category
class ChildCategory(models.Model):
    name = models.CharField(max_length=255,null=True, blank =True);

    class Meta:
        verbose_name = 'Child Category'
        verbose_name_plural = 'Child Category'

    def __str__(self):
        return str(self.name)



# child category
class ChildGender(models.Model):
    name = models.CharField(max_length=255,null=True, blank =True);

    class Meta:
        verbose_name = 'Child Gender'
        verbose_name_plural = 'Child Gender'

    def __str__(self):
        return str(self.name)

    # children registration table
class RegisteredChildren(models.Model):
    user = models.ForeignKey(User,null=True, blank =True)
    registration_date = models.DateTimeField(null=True, blank =True);
    name  = models.CharField(max_length=255,null=True, blank =True);
    age = models.IntegerField(null=True, blank =True);
    dob = models.DateTimeField(null=True, blank =True);
    category = models.ForeignKey(ChildCategory,null=True, blank =True)
    gender = models.ForeignKey(ChildGender,null=True, blank =True)
    schoolAdmission = models.BooleanField(default=False)
    schoolName = models.CharField(max_length=255,null=True, blank =True)
    locationOfChild = models.TextField(null=True, blank =True)
    childFoundTime = models.TimeField(null=True, blank =True)
    parentsEmployment = models.BooleanField(default=False)
    parentsLocationOfWork = models.TextField(null=True, blank =True)
    income = models.IntegerField(null=True, blank =True)
    imageOfChild = models.ImageField(null=True, blank =True,upload_to= get_image_upload_dir(["child_registrations",]))
    birthMark = models.ImageField(null=True, blank =True)




    class Meta:
        verbose_name = 'Child Registration Information'
        verbose_name_plural = 'Child Registration Information'


    def __str__(self):
        return str(self.name)




class OrphanageNgo(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True);
    email = models.CharField(max_length=255, null=True, blank=True);

    def __str__(self):
        return str(self.name)

class MedicalCheckup(models.Model):
    child  = models.ForeignKey(RegisteredChildren, null=True, blank=True)
    assignedTo = models.ForeignKey(OrphanageNgo, null=True, blank=True)
    medicalCheckupStatus = models.BooleanField() ;
    medicalReason = models.TextField(null=True, blank =True)

    def __str__(self):
        return str(self.child.name)





    # Police criminal record table
class PoliceCriminalRecord(models.Model):
    registration_date = models.DateTimeField(null=True, blank =True);
    name = models.CharField(max_length=255,null=True, blank =True);
    age = models.IntegerField(null=True, blank =True);
    dob = models.DateTimeField(null=True, blank =True);
    gender = models.ForeignKey(ChildGender,null=True, blank =True)
    schoolAdmission = models.BooleanField()
    schoolName = models.CharField(max_length=255,null=True, blank =True)
    locationOfChild = models.TextField(null=True, blank =True)
    parentsEmployment = models.BooleanField()
    parentsLocationOfWork = models.TextField(null=True, blank =True)
    income = models.IntegerField(null=True, blank =True)
    criminalRecordDescription = models.TextField(null=True, blank =True)
    medicalRecord = models.BooleanField()
    medicalRecordDescription = models.TextField(null=True, blank =True)
    imageOfChild = models.ImageField(null=True, blank =True,upload_to= get_image_upload_dir(["criminal_records",]))


    class Meta:
        verbose_name = 'Police Criminal Records'
        verbose_name_plural = 'Police Criminal Records'

    def save(self, *args, **kwargs):

        super(PoliceCriminalRecord, self).save(*args, **kwargs)
        np.savetxt(get_image_upload_dir(["Media","criminal_records","encoding"])+str(self.id)+'.txt', face_recognition.face_encodings(face_recognition.load_image_file("Media/"+self.imageOfChild.name))[0])

    def __str__(self):
        return str(self.name)



# Police lost and found record table
class LostAndFoundRecords(models.Model):
    registration_date = models.DateTimeField(null=True, blank =True);
    name = models.CharField(max_length=255,null=True, blank =True);
    age = models.IntegerField(null=True, blank =True);
    gaurdianName = models.CharField(max_length=255,null=True, blank =True)
    gender = models.ForeignKey(ChildGender,null=True, blank =True)
    schoolAdmission = models.BooleanField()
    schoolName = models.CharField(max_length=255,null=True, blank =True)
    locationOfChildLost = models.TextField(null=True, blank =True)
    locationToContact = models.TextField(null=True, blank =True)
    gaurdianContactNumber = models.IntegerField(null=True, blank =True)
    imageOfChild = models.ImageField(null=True, blank =True,upload_to= get_image_upload_dir(["lost_and_found_records",]))

    def save(self, *args, **kwargs):
        super(LostAndFoundRecords, self).save(*args, **kwargs)
        np.savetxt(get_image_upload_dir(["Media","lost_and_found_records","encoding"])+str(self.id)+'.txt', face_recognition.face_encodings(face_recognition.load_image_file("Media/"+self.imageOfChild.name))[0])


    class Meta:
        verbose_name = 'Lost and Found records'
        verbose_name_plural = 'Lost and Found records'


    def __str__(self):
        return str(self.name)







from django.db import models

# Create your models here.
