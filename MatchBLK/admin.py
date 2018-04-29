from django.contrib import admin
from .models import SignUp,MentorSkill,MenteeSkill

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.shortcuts import redirect

class MentorSkillAdmin(admin.TabularInline):
    model = MentorSkill
    extra = 1

class MenteeSkillAdmin(admin.TabularInline):
    model = MenteeSkill
    extra = 1

class SignUpAdmin(admin.ModelAdmin):

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/BLK/5/results')

    def response_change(request, obj):
        return redirect('/BLK/5/results')

    def save_model(self, request, obj, form, change):

        obj.save()
    inlines = [MenteeSkillAdmin,MentorSkillAdmin]

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(SignUp,SignUpAdmin)