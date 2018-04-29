# Generated by Django 2.0.4 on 2018-04-28 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenteeSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menteeskills', models.CharField(choices=[('PYTHON', 'PYTHON'), ('JAVA', 'JAVA'), ('SQL', 'SQL'), ('DATA SCIENCE', 'DATA SCIENCE')], max_length=25)),
                ('other', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MentorSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mentorskills', models.CharField(choices=[('Empty', 'Please select skill(s) '), ('PYTHON', 'PYTHON'), ('JAVA', 'JAVA'), ('SQL', 'SQL'), ('DATA SCIENCE', 'DATA SCIENCE')], default='Empty', max_length=30)),
                ('Mentorskill_level', models.CharField(choices=[('Empty', 'Please select skill level '), ('ADVANCED', 'ADVANCED'), ('INTERMEDIATE ', 'INTERMEDIATE'), ('BEGINNER', 'BEGINNER')], default='Empty', max_length=30)),
                ('other', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mentor', models.BooleanField()),
                ('mentee', models.BooleanField()),
                ('virtual_mentorship', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='YES', max_length=10)),
                ('number_of_mentees', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (5, 5)], default=1)),
                ('interest', models.TextField(max_length=50, null=True)),
                ('purpose', models.TextField(max_length=50, null=True)),
                ('other', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='mentorskill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mentorlist', to='MatchBLK.SignUp'),
        ),
        migrations.AddField(
            model_name='menteeskill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='menteelist', to='MatchBLK.SignUp'),
        ),
    ]