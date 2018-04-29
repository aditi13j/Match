from django.db import models
from multiselectfield import MultiSelectField

# the following lines added:
import datetime
from django.utils import timezone

NUMBER_OF_MENTEE_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (5, 5),

)
MENTOR_SKILL_LEVEL_CHOICES = (
    ("Empty", "Please select skill level "),
    ("ADVANCED", "ADVANCED"),
    ("INTERMEDIATE ", "INTERMEDIATE"),
    ("BEGINNER", "BEGINNER"),

)
SKILL_CHOICES = (
    ("Empty" , "Please select skill(s) "),
    ("PYTHON", "PYTHON"),
    ("JAVA", "JAVA"),
    ("SQL", "SQL"),
    ("DATA SCIENCE", "DATA SCIENCE"),

)
MENTEE_SKILL_CHOICES = (
    ("PYTHON", "PYTHON"),
    ("JAVA", "JAVA"),
    ("SQL", "SQL"),
    ("DATA SCIENCE", "DATA SCIENCE"),

)
VIRTUAL_MEMBERSHIP_LIST = (
    ("Yes","Yes"),
    ("No","No"),
)

class SignUp(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    mentor = models.BooleanField()
    mentee = models.BooleanField()
    virtual_mentorship = models.CharField(max_length=10, choices=VIRTUAL_MEMBERSHIP_LIST, default="YES")
    number_of_mentees = models.IntegerField(choices=NUMBER_OF_MENTEE_CHOICES, default=1)
    interest = models.TextField(max_length=50,null=True)
    purpose = models.TextField(max_length=50,null=True)
    other = models.CharField(max_length=20,null=True)


    def __str__(self):
        return self.first_name


class MentorSkill(models.Model):
    user = models.ForeignKey(SignUp,on_delete=models.PROTECT,related_name='mentorlist')
    Mentorskills = models.CharField(max_length=30, choices=SKILL_CHOICES, default="Empty")
    Mentorskill_level = models.CharField(max_length=30, choices=MENTOR_SKILL_LEVEL_CHOICES, default="Empty")
    other = models.CharField(max_length=20)

    def __str__(self):
        return self.other

class MenteeSkill(models.Model):
    user = models.ForeignKey(SignUp,on_delete=models.PROTECT,related_name='menteelist')
    menteeskills = models.CharField(max_length=25,choices=MENTEE_SKILL_CHOICES)
    other = models.CharField(max_length=20)

    def __str__(self):
        return self.other


