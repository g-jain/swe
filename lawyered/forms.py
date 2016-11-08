from django import forms
from django.contrib.auth.models import User
import datetime
from .models import *

#login
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#register   
class UserRegistrationForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        ('c', 'Client'),
        ('l', 'Lawyer' ),
    )

    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    type_user = forms.CharField(widget = forms.HiddenInput(), initial='c', max_length = 250)
    area= forms.CharField(label = 'In which city do you practice in?', max_length = 250)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']

#question for forum
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', 'tags')

#forum
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture','type_user')

class LawyerProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('type_user','specialization', 'area')
    
class LawyerRegistrationForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        ('c', 'Client'),
        ('l', 'Lawyer' ),
    )
    CHOICES9 = (('1','Divorce'),('2','Dui'),('3','Criminal'),('4','Family'),('5','Merger'),('6','Estate'))
    type_user = forms.CharField(initial='l', max_length = 250, disabled = True)
    first_name = forms.CharField(label = 'Enter your first name', max_length = 250)
    last_name = forms.CharField(label = 'Enter your last name?', max_length = 250)
    area = forms.CharField(label = 'In which city do you practice in?', max_length = 250)
    specialization = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = CHOICES9, label = 'What is your area of specialization?')
    details = forms.CharField(label = 'Please enter more about you', max_length = 1000, required=False)
    #image = No idea
    image=models.ImageField(upload_to='lawyered/media', blank=True )
    contact = forms.CharField(label = 'Enter your contact number', max_length = 12)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email')

#search in forum
class SearchForm(forms.Form):
    query = forms.CharField()
ASSETS = (
    ('Residential Property', 'Residential Property'),
    ('Investmant Property', 'Investmant Property'),
    ('Investment Account(s) (Stocks, Bonds, Mutual Funds, etc.)', 'Investment Account(s) (Stocks, Bonds, Mutual Funds, etc.)'),
    ('Bank Account(s)','Bank Account(s)'),
    ('Pension, Or Other Retirement Plans', 'Pension, Or Other Retirement Plans'),
    ('Business Interest(s)','Business Interest(s)'),
    ('Personal Property (Jewellery, Cars, Furniture, Appliances, etc.)','Personal Property (Jewellery, Cars, Furniture, Appliances, etc.)'),
    ('Others','Others'),
    )
TESTS = ( 
    ('Breathalyzer','Breathalyzer'),
    ('Balance And Cordination Tests','Balance And Coordination Tests'),
    ('Eye Movement Test (Pen Test)','Eye Movement Test (Pen Test)'),
    ('Blood Test','Blood Test'),
    ('Other','Other'),
    )

REASONS = (
    ('Speeding','Speeding'),('Swerving','Swerving'), ('Illegal Maneuver','Illegal Maneuver'),
    ('Reckless Driving','Reckless Driving'), ('Equipment Violation (Missing Headlight, Excessive Window Tinting, etc.)','Equipment Violation (Missing Headlight, Excessive Window Tinting, etc.)'),
    ('DUI Checkpoint','DUI Checkpoint'), ('Other','Other'),
    )

SITUATION = (
    ('I Was Questioned','I Was Questioned'),
    ('I Was Detained','I Was Detained'),
    ('I Was Arrested','I Was Arrested'),
    ('I Was Formally Charged With A Crime','I Was Formally Charged With A Crime')
    )

CHOICES1 = (('Yes', 'Yes',), ('No', 'No',),('Not Sure','Not Sure',))
CHOICES2 = (('Male', 'Male',), ('Female', 'Female',))
CHOICES3 = (('Yes', 'Yes',), ('No', 'No',))
CHOICES4 = (('Morning','Morning'),('Afternoon','Afternoon'),('Evening','Evening'),('Late Night','Late Night'))
CHOICES5 = (('No','No'),('Yes, I Do','Yes, I Do'),('Yes, My Partner Does','Yes, My Partner Does'),
    ('Yes, We Both Do','Yes, We Both Do'),('I\'m Not Sure','I\'m Not Sure'))
CHOICES6 = (('Buying A Business','Buying A Business'),('Selling A Business','Selling A Business'),('Merging With Another Company','Merging With Another Company'))
CHOICES7 = (('Buying an Estate','Buying An Estate'),('Selling An Estate','Selling An Estate'))
CHOICES8 = (('Condominium','Condominium'),('Single Family Home','Single Family Home'),('Multi-Family Complex','Multi-Family Complex'),
    ('Office Building','Office Building'),('Shopping Center','Shopping Center'),('Land','Land'),('Industrial','Industrial'),('Other','Other'))

class divorcecaseForm(forms.ModelForm):    
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES2, label = 'Gender of your spouse?')
    mutual = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES1, label = 'Was a pre-nuptial agreement in place at the time of marriage?')
    assets = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=ASSETS, label = 'What Assets did spouse have before marriage? (Select All that Apply)')
    assets_before = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=ASSETS, label = 'What Assets did spouse acquire after marriage? (Select All that Apply)')
    children = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES3, label = 'Do you have children?')
    custody = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES1, label = 'Will either spouse be asking for child support?')

    class Meta:
        model = divorceForm
        fields = [
            'name',
            'spouse',
            'date_of_marriage',
            'gender',
            'mutual',
            'assets',
            'assets_before',
            'children',
            'custody',
            'budget',
            'details',
        ]

class duiCaseForm(forms.ModelForm):
    date_of_citation = forms.DateField(initial = datetime.date.today , label = 'When did you receive the DUI citation?')
    tests = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices = TESTS,label =  'What sobriety tests did the officer perform to measure your intoxication level? (Select all that apply)')
    bac = forms.DecimalField(label = 'If applicable, What was your Blood Alcohol Content (BAC)?',decimal_places=2)
    time_of_day = forms.ChoiceField(widget = forms.RadioSelect, label = 'What time of day were you pulled over?', choices = CHOICES4)
    reason = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = REASONS, label = 'Why were you pulled Over? (Select all that apply)')
    past = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES3, label = 'Have you had a DUI in the past?')
    next_date = forms.DateField(initial = datetime.date.today, label = 'When is your next court date?')
    #budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2)
    details = forms.CharField(label = 'Further Details')

    class Meta:
        model = duiForm
        fields = [
            'name','date_of_citation','tests','bac','time_of_day',
            'reason','past','next_date','budget','details',
        ]
        

class criminalCaseForm(forms.ModelForm):
    offense = forms.CharField(label = 'What is the name of the offense?')
    offense_date = forms.DateField(initial = datetime.date.today, label = 'What date did the incident occur?')
    situation = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = SITUATION, label = 'Which of the following best describe your situation?')
    agency = forms.CharField(label = 'What was the law enforcement agency involved?')
    court_past = forms.ChoiceField(widget = forms.RadioSelect, label = 'Have you already been to court for this matter?', choices = CHOICES3)
    next_date = forms.DateField(initial = datetime.date.today, label = 'When is your next court date?')
    worked = forms.ChoiceField(widget = forms.RadioSelect ,label = 'Have you previously worked with a lawyer on this matter?', choices = CHOICES3)
    #budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2)
    details = forms.CharField(label = 'Further Details')

    class Meta:
        model = criminalForm
        fields = [
            'name','offense','offense_date','situation','agency',
            'court_past','next_date','worked','budget','details',
        ]

class prenupCaseForm(forms.ModelForm):
    partner = forms.CharField(label = 'What is your partner\'s name?', max_length = 25)
    assets = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, choices = ASSETS, 
    label = 'Which assests do you own that will be part of the pre-nuptial agreement? (Select all that apply)')
    debt = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES5, label = 'Do you or your partner have any debt?')
    debt_details = forms.CharField(label = 'If yes, please explain the type of the debt and approximate amount')
    assets_exclude = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES1, 
    label = 'Are there any assets that you or your partner would like to exclude from the pre-nuptial agreement?')
    exclude_details = forms.CharField(label = 'If yes, Please explain')
    #budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2)
    
    class Meta:
        model = prenupForm
        fields = [
            'name','partner','assets','debt','debt_details',
            'assets_exclude','exclude_details','budget',
        ]


class mergerCaseForm(forms.ModelForm):
    types = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES6, label = 'Which of the following do you need help?')
    names = forms.CharField(label  = 'What are the names of all the parties involved in the transaction?')
    circumstances = forms.CharField(label = 'Describe the circumstances of the sale or merger in as much details as possible:')
    need = forms.CharField(label = 'What do you need a lawyer to help with?')
    #budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2)

    class Meta:
        model = mergerForm
        fields = [
            'name','types','names','circumstances','need','budget',
        ]

class estateCaseForm(forms.ModelForm):
    types  = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES7, label = 'What do you want to do?')
    property_type = forms.ChoiceField(widget = forms.RadioSelect, choices = CHOICES8, label = 'What type of property is involved?')
    details = forms.CharField(label= 'Describe your legal issues in as much details as possible:')
    need = forms.CharField(label = 'What do you need a lawyer to help with?')
    #budget = forms.DecimalField(label='What is your estimated budget?',max_digits=6, decimal_places=2)

    class Meta:
        model = estateForm
        fields = [
            'name','types','property_type','details','need','budget',
        ]