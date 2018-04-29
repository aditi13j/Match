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

    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id): #can have user level details
    #logic to retreive Top matches

    return HttpResponse("Hello!, meet %s!" % question_id)

def results(request, question_id):
    user_list = models.SignUp.objects.all()
    result_list = []
    for item in user_list:
        item.first_name = "James"

        result_list.append(item)
        print(item.last_name)

    context = {'result_list': result_list}
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