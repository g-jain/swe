from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django_markdown.models import MarkdownField


class UserProfile(models.Model):
	USER_TYPE_CHOICES = (
		('c', 'Client'),
		('l', 'Lawyer' ),
	)

	user = models.OneToOneField(User)
	points = models.IntegerField(default=0)
	type_user = models.CharField(max_length=250, choices=USER_TYPE_CHOICES, blank=True)
	first_name = models.CharField(max_length=250,default='.')
	last_name = models.CharField(max_length=250,default='.')
	area = models.CharField(max_length=250, default='.')
	contact = models.IntegerField(default= 0)
	specialization = models.CharField(max_length=250,default='.')
	bar_no = models.IntegerField(default=0)
	details = models.TextField(max_length=1000, default='.')
	picture = models.ImageField(upload_to='lawyered/media/',blank=True)
	website = models.URLField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username
	
class person(models.Model):
	name = models.CharField(max_length=250)
	area = models.CharField(max_length=250)
	specialization = models.CharField(max_length=250)
	details = models.TextField()
	image = models.ImageField(upload_to='lawyered/media/',blank=True)
	def __str__(self):
		return self.name	

#userprofile
#class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
#    user = models.OneToOneField(User)
#    points = models.IntegerField(default=0)

    # The additional attributes we wish to include.
#    website = models.URLField(blank=True)
#    picture = models.ImageField(upload_to='qa/static/profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
#    def __unicode__(self):
#        return self.user.username
	
#tags for forum
class Tag(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('slug',)

#forum question
class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    tags = models.ManyToManyField(Tag)
    reward = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    user_data = models.ForeignKey(UserProfile)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

#forum answer
class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = MarkdownField()
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    user_data = models.ForeignKey(UserProfile)
    def __str__(self):
        return self.answer_text

#forum voter
class Voter(models.Model):
    user = models.ForeignKey(UserProfile)
    answer = models.ForeignKey(Answer)

#forum votes
class QVoter(models.Model):
    user = models.ForeignKey(UserProfile)
    question = models.ForeignKey(Question)

#forum comment
class Comment(models.Model):
    answer = models.ForeignKey(Answer)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user_data = models.ForeignKey(UserProfile)
    def __str__(self):
        return self.comment_text

#divorce form
class divorceForm(models.Model):
	
#	name = models.ForeignKey(UserProfile)
	name = models.CharField(max_length=250)
	spouse = models.CharField('What is your Spouse\'s name?', max_length = 25)
	date_of_marriage = models.DateField( 'What was your Date of Marriage?',default=datetime.date.today)
	gender = models.CharField(max_length=250)
	mutual = models.CharField(max_length=250)
	assets = models.CharField(max_length=250)
	assets_before = models.CharField(max_length=250)
	children = models.CharField(max_length=250)
	custody = models.CharField(max_length=250)
	budget = models.CharField(max_length=250)
	details = models.CharField(max_length=250)
	casetype = models.CharField(max_length=250, default="Divorce")
	
class duiForm(models.Model):
	name = models.CharField(max_length=250)
	date_of_citation = models.DateField('When did you receive the DUI citation?', default = datetime.date.today)
	tests = models.CharField(max_length=250)
	bac = models.DecimalField(max_digits=6,decimal_places=2)
	time_of_day = models.CharField(max_length=250)
	reason = models.CharField(max_length=250)
	past = models.CharField(max_length=250)
	next_date = models.DateField(default = datetime.date.today)
	budget = models.CharField(max_length=250)
	details = models.CharField(max_length=250)
	casetype = models.CharField(max_length=250, default="Dui")
	
class criminalForm(models.Model):
	name = models.CharField(max_length=250)
	offense = models.CharField(max_length=250)
	offense_date = models.DateField(default = datetime.date.today)
	situation = models.CharField(max_length=250)
	agency = models.CharField(max_length=250)
	court_past = models.CharField(max_length=250)
	next_date = models.DateField(default = datetime.date.today)
	worked = models.CharField(max_length=250)
	budget = models.CharField(max_length=250)
	details = models.CharField(max_length=250)
	casetype = models.CharField(max_length=250, default="Criminal")
	

class prenupForm(models.Model):
	name = models.CharField(max_length=250)
	partner = models.CharField(max_length=250)
	assets = models.CharField(max_length=250)
	debt = models.CharField(max_length=250)
	debt_details = models.CharField(max_length=250)
	assets_exclude = models.CharField(max_length=250)
	exclude_details = models.CharField(max_length=250)
	budget = models.CharField(max_length=250)
	casetype = models.CharField(max_length=250, default="Family")

class mergerForm(models.Model):
	name = models.CharField(max_length=250)
	types = models.CharField(max_length=250)
	names = models.CharField(max_length=250)
	circumstances = models.CharField(max_length=250)
	need = models.CharField(max_length=250)
	budget = models.CharField(max_length=250)
	casetype = models.CharField(max_length=250, default="Merger")

class estateForm(models.Model):
	name = models.CharField(max_length=250)
	types = models.CharField(max_length=250)
	property_type = models.CharField(max_length=250)
	details = models.CharField(max_length=250)
	need = models.CharField(max_length=250)
	budget = models.CharField(max_length=250)
	casetype = models.CharField(max_length=250, default="Estate")