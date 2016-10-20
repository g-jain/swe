from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django_markdown.models import MarkdownField


class person(models.Model):
	name = models.CharField(max_length=250)
	area = models.CharField(max_length=250)
	specialization = models.CharField(max_length=250)
	details = models.TextField()
	image = models.ImageField(upload_to='lawyered/media/',blank=True)
	def __str__(self):
		return self.title	

#userprofile
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='qa/static/profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
	
#tags for forum
class Tag(models.Model):
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('slug',)

#forum question
class Question(models.Model):
    question_text = models.CharField(max_length=200)
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
	ASSETS = (
    ('residential_property', 'Residential Property'),
    ('investment_property', 'Investmant Property'),
    ('investment_account', ' Investment Account(s) (stocks, bonds, mutual funds, etc.) '),
    ('bank_account','Bank Account(s)'),
    ('pension', 'pension, or other retirement plan'),
    ('business','Business interest(s)'),
    ('personal_property','Personal property (jewelry, cars, furniture, appliances, etc.) '),
    ('others','Others'),
    )
	CHOICES1 = (('1', 'Yes',), ('2', 'No',),('3','Not Sure',))
	CHOICES2 = (('1', 'Male',), ('2', 'Female',))
	CHOICES3 = (('1', 'Yes',), ('2', 'No',))

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
	casetype = models.CharField(max_length=250, default="divorce")

