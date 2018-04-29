from rest_framework import serializers
from .models import SignUp,MentorSkill

class MentorSkills(serializers.ModelSerializer):
    class Meta:
        model = MentorSkill
        fields = (
                  'Mentorskills',
                  'Mentorskill_level',
                  )
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return MentorSkill.objects.create(**validated_data)



class SignUp(serializers.ModelSerializer):
    mentorlist = MentorSkills(many=True)

    class Meta:
        model = SignUp
        fields = ('first_name',
                  'last_name',
                  'email',
                  'mentor',
                  'mentee',
                  'virtual_mentorship',
                  'number_of_mentees',
                  'interest',
                  'purpose',
                  'mentorlist',

                  )

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        items_data = validated_data.pop('items')
        signup_list = SignUp.objects.create(**validated_data)
        for item_data in signup_list:
            MentorSkill.objects.create(**item_data)
        return SignUp.objects.create(**validated_data)

