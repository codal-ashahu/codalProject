from __future__ import unicode_literals

from django.db import models

ROLE_CHOICES = (
    ('TL', 'TL'),
    ('PM', 'PM'),
    ('Dev', 'Dev'),
)

class Skill(models.Model):
    skill = models.CharField(max_length=255, blank=False, null=False)
    def __unicode__(self):
        return str(self.skill)
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    role = models.CharField(
        choices=ROLE_CHOICES, max_length=20,
        default="Dev")
    skills = models.ManyToManyField(
        Skill, related_name="people_with_skill", blank=True)
    def __unicode__(self):
        return str(self.name)

class Project(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    project_manager = models.ManyToManyField(
        Person, related_name="pm_in_projects", blank=True,
        limit_choices_to={'role': 'PM'})
    team_lead = models.ManyToManyField(
        Person, related_name="tl_in_projects", blank=True,
        limit_choices_to={'role': 'TL'})
    developers = models.ManyToManyField(
        Person, related_name="dev_in_projects", blank=True,
        limit_choices_to={'role': 'Dev'})
    def __unicode__(self):
        return str(self.name)

