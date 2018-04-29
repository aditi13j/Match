from django.db import models


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
    ("Advanced", "Advanced"),
    ("Intermediate ", "Intermediate"),
    ("Beginner", "Beginner"),

)
SKILL_CHOICES = (
    ("Empty" , "Please select skill(s)"),
    ("Artificial Intelligence", "ArtificialIntelligence"),
    ("DataAnalysis", "Data Analysis"),
    ("Presentation Skills", "Presentation Skills"),
    ("Communication", "Communication"),
    ("Python", "Python"),
    ("Database", "Database"),
    ("UX Design", "UX Design"),
    ("Project Management", "Project Management"),
    ("Portfolio Management", "Portfolio Management"),
    ("Investment Systems", "Investment Systems"),
    ("Leadership Skill", "Leadership Skill"),
)

PURPOSE_CHOICES = (
    ("Empty", "Please select a Purpose questions"),
    ("As a BLK employee, where can you have the biggest impact on society?", "As a BLK employee,where can you have the biggest impact on society"),
    ("What is your personal definition of wellbeing?", "What is your personal definition of wellbeing?"),
    ("Where do you believe BlackRock can have the biggest impact on society?", "Where do you believe BlackRock can have the biggest impact on society?"),
    ("Tell me about a unique area of expertise that you're proud of", "Tell me about a unique area of expertise that you're proud of"),
    ("What makes you most proud to be a part of BlackRock?", "What makes you most prod to be a part of BlackRock?"),
    ("What do you most want people to know about BlackRock?", "What do you most want people to know about BlackRock?"),

)

MENTEE_SKILL_CHOICES = (
    ("What are the new areas of expertise that you're trying to develop?", "What are the new areas of expertise that you're trying to develop?"),

)
VIRTUAL_MEMBERSHIP_LIST = (
    ("Yes","Yes"),
    ("No","No"),
)

class SignUp(models.Model):
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    email = models.EmailField()
    mentor = models.BooleanField()
    mentee = models.BooleanField()
    virtual_Mentorship= models.CharField(max_length=10, choices=VIRTUAL_MEMBERSHIP_LIST, default="YES")
    number_of_Mentees = models.IntegerField(choices=NUMBER_OF_MENTEE_CHOICES, default=1)


    Other_Interests = models.TextField(max_length=500,null=True)
    Living_Our_Purpose = models.CharField(max_length=300, choices=PURPOSE_CHOICES, default="Empty")
    Ans = models.TextField(max_length=50,null=True)

    Mentee_Skills = models.CharField(max_length=300, choices=MENTEE_SKILL_CHOICES, default="Empty")

    Artificial_Intelligence = models.BooleanField()
    Data_Analysis = models.BooleanField()
    Presentation_Skills = models.BooleanField()
    Communication = models.BooleanField()
    Python = models.BooleanField()
    Database = models.BooleanField()
    UX_Design = models.BooleanField()
    Project_Management = models.BooleanField()
    Portfolio_Management = models.BooleanField()
    Investment_Systems = models.BooleanField()
    Leadership_Skill = models.BooleanField()



    def __str__(self):
        return self.first_Name


class MentorSkill(models.Model):
    user = models.ForeignKey(SignUp,on_delete=models.PROTECT,related_name='mentorlist')
    Mentorskills = models.CharField(max_length=30, choices=SKILL_CHOICES, default="Empty")
    Mentorskill_level = models.CharField(max_length=30, choices=MENTOR_SKILL_LEVEL_CHOICES, default="Empty")


    def __str__(self):
        return self.Mentorskills


