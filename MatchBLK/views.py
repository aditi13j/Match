from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from MatchBLK import serializer, models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
import random
from django.http import HttpResponse, HttpResponseRedirect

class SignUp(APIView):
    def get(self,request,format = None):
        all_objects = models.SignUp.objects.all()
        s = serializer.SignUp(all_objects, many=True)
        return Response(s.data)

    def post(self,request,format = None):
        serializer = serializers.SignUp(data=request.data)
        if serializer.is_valid():
            # then save the ToDoList to the database and return the resulting ToDoList
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'MatchBLK/index.html')


def detail(request,question_id): #can have user level details
    #logic to retreive Top matches

    return HttpResponse("Hello!, meet %s!" % question_id)

def results(request, question_id):
    user_list = models.SignUp.objects.all()
    maxID = -1
    for user in user_list:
        maxID = max(user.id, maxID)

    skills_to_match = models.SignUp.objects.get(id = maxID)


    # print (input_user_list)
    result_list = []

    master_skill = [
        'Artificial Intelligence','Data Analysis','Presentation Skills','Python','Database','UX Design',
        'Project Management' , 'Portfolio Management', 'Investment Systems',
        'Leadership Skill' , 'Communication' , 'Problem Solving' , 'Negotiation and Conflict Resolution '
        'Time Management'
         ]

    first_names = ('John', 'Andy', 'Joe','Isaac','Sarah', 'Mary', 'Nancy', 'Tom')
    last_names = ('Johnson', 'Smith', 'Williams' , 'Newton')

    for items in user_list:
        input_user_list = []

        if(skills_to_match.Artificial_Intelligence):
            input_user_list.append('Artificial Intelligence')
        if (skills_to_match.Data_Analysis):
            input_user_list.append('Data Analysis')
        if (skills_to_match.Presentation_Skills):
            input_user_list.append('Presentation Skills')
        if (skills_to_match.Python):
            input_user_list.append('Python')
        if (skills_to_match.Database):
            input_user_list.append('Database')

        new_user = []
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        new_user.append(first_name)
        new_user.append(last_name)
        new_user.append(first_name.lower()+"."+last_name.lower()+"@blackrock.com")

        new_user_skills = []

        #add skills
        random_length_user_list = random.randrange(1, len(input_user_list))
        new_user_skills.append(input_user_list[0])
        for i in range(1,random_length_user_list):
            new_user_skills.append(input_user_list[i])

        random_length_master_skill = random.randrange(1, len(master_skill))
        for i in range(1,random_length_master_skill):
            new_user_skills.append(master_skill[i])


        new_user.append(list(set(new_user_skills)))
        result_list.append(new_user)


    context = {'result_list': result_list[:3],
               }
    return render(request, 'MatchBLK/results.html', context)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


class CreateSignup(CreateView):
    model = models.SignUp
    fields = ['first_name',
              'last_name',
              'email',
              'mentor',
              'mentee',
              'open_for_virtual_mentorship',
              'number_of_mentees',
              'interest',
              'purpose',
              'mentorlist',
              'menteelist'
              ]