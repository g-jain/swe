from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
import datetime


# Create your views here.
def index(request) :
	return render(request, 'lawyered/index.html')
	
def login_view(request):
	if request.method== 'POST':

		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			username = form.cleaned_data['username']
			if user is not None:
				login(request,user)
				return render(request,'lawyered/dashboard.html', {'username': username})
			else:
				return render(request, 'lawyered/invalid.html')

	else:
		form = LoginForm()
		return render(request, 'lawyered/login.html', {'form': form})

def forumlogin(request):
    if request.method== 'POST':
    	form = LoginForm(request.POST)
    	if form.is_valid():
    		cd = form.cleaned_data
    		user = authenticate(username=cd['username'], password=cd['password'])
    		username = form.cleaned_data['username']
    		if user is not None:
    			login(request,user)
    			return render(request,'lawyered/forum.html', {'username': username})
    		else:
    			return render(request, 'lawyered/invalid.html')
    else:
    	form = LoginForm()
    	return render(request, 'lawyered/login.html', {'form': form})

    
	
def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            return render(request,'lawyered/register_done.html')
        else:
            print (user_form.errors, profile_form.errors)

    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request,'lawyered/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def dashboard(request):
	username = request.user.username
	divcases = divorceForm.objects.filter(name__contains = username)
	duicases = duiForm.objects.filter(name__contains = username)
	cricases = criminalForm.objects.filter(name__contains = username)
	precases = prenupForm.objects.filter(name__contains = username)
	mercases = mergerForm.objects.filter(name__contains = username)
	estcases = estateForm.objects.filter(name__contains = username)
	# Add a piece of code for all forms
	return render(request, 'lawyered/dashboard.html', {'username': username, 'divcases':divcases, 'duicases':duicases, 'cricases' : cricases,'mercases': mercases, 'precases' : precases, 'estcases' : estcases })

#Now get all lawyer objects
def person_list(request):
	persons = person.objects.all()
	query = request.GET.get("q")
	if query:
		persons = persons.filter(area__contains = query)
	return render(request,'lawyered/search.html',{'persons': persons, 'username':request.user.username})

#	
def search_question(request):
    if request.method == 'POST':
        word = request.POST['word']
        latest_question_list = Question.objects.filter(question_text__contains=word)
        paginator = Paginator(latest_question_list, 10)
        page = request.GET.get('page')
        try:
            questions = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            questions = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            questions = paginator.page(paginator.num_pages)

        latest_noans_list = Question.objects.order_by('-pub_date').filter(tags__slug__contains=word,answer__isnull=True)[:10]
        top_questions = Question.objects.order_by('-reward').filter(tags__slug__contains=word,answer__isnull=True,reward__gte=1)[:10]
        count = Question.objects.count
        count_a = Answer.objects.count

        template = loader.get_template('lawyered/forum.html')
        context = {
        'questions': questions,
        'totalcount': count,
        'anscount': count_a,
        'noans': latest_noans_list,
        'reward': top_questions,
        }
    return render(request,'lawyered/forum.html', context)

def tag(request, tag):
    word = tag
    latest_question_list = Question.objects.filter(tags__slug__contains=word)
    paginator = Paginator(latest_question_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    latest_noans_list = Question.objects.order_by('-pub_date').filter(tags__slug__contains=word,answer__isnull=True)[:10]
    top_questions = Question.objects.order_by('-reward').filter(tags__slug__contains=word,answer__isnull=True,reward__gte=1)[:10]
    count = Question.objects.count
    count_a = Answer.objects.count

    template = 'lawyered/forum.html'
    context = request, {
    'questions': questions,
    'totalcount': count,
    'anscount': count_a,
    'noans': latest_noans_list,
    'reward': top_questions,
    }
    return render(request, template,context)


def forum(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    latest_noans_list = Question.objects.order_by('-pub_date').filter(answer__isnull=True)[:10]
    top_questions = Question.objects.order_by('-reward').filter(answer__isnull=True,reward__gte=1)[:10]

    count = Question.objects.count
    count_a = Answer.objects.count

    paginator = Paginator(latest_question_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)

    template = 'lawyered/forum.html'
    context = {
        'questions': questions,
        'totalcount': count,
        'anscount': count_a,
        'noans': latest_noans_list,
        'reward': top_questions,
    }
    return render(request, 'lawyered/forum.html',context)


def profile(request, user_id):
    user_ob = User.objects.get(id=user_id)
    user = UserProfile.objects.get(user=user_ob)
    return render(request, 'lawyered/profile.html', {'user': user})

def add(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect("/login/")

	if request.method == 'POST':
		question_text = request.POST['question']
		tags_text = request.POST['tags']
		user_id = request.POST['user']
		user_ob = User.objects.get(id=user_id)
		user = UserProfile.objects.get(user=user_ob)

		if question_text.strip() == '':
			return render(request, 'lawyered/add.html', {'message': 'Empty'})

		pub_date = datetime.datetime.now()
		q = Question()
		q.question_text = question_text
		q.pub_date = pub_date
		q.user_data = user
		q.save()

		tags = tags_text.split(',')
		for tag in tags:
			try:
				t = Tag.objects.get(slug=tag)
				q.tags.add(t)
			except Tag.DoesNotExist:
				t=Tag()
				t.slug = tag
				t.save()
				q.tags.add(t)
     
		return HttpResponseRedirect('/lawyered/forum')
	return render(request, 'lawyered/add.html')
#    return HttpResponse(template.render(context))

@login_required
def comment(request, answer_id):

    if request.method == 'POST':
        comment_text = request.POST['comment']
        user_id = request.POST['user']
        user_ob = User.objects.get(id=user_id)
        user = UserProfile.objects.get(user=user_ob)
        user.points += 1
        user.save()

        if comment_text.strip() == '':
            return render(request, 'lawyered/comment.html', {'answer_id': answer_id, 'message': 'Empty'})

        pub_date = datetime.datetime.now()
        a = Answer.objects.get(pk=answer_id)
        q_id = a.question_id
        c = Comment()
        c.answer = a
        c.comment_text = comment_text
        c.pub_date = pub_date
        c.user_data = user
        c.save()

        try:
            question = Question.objects.get(pk=q_id)
            question.views += 1
            question.save()
            answer_list = question.answer_set.order_by('-votes')

            paginator = Paginator(answer_list, 10)
            page = request.GET.get('page')
            try:
                answers = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                answers = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                answers = paginator.page(paginator.num_pages)

        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'lawyered/detail.html', {'answers': answers, 'question': question}, )

    template = loader.get_template('lawyered/comment.html')
    context = RequestContext(request, {'answer_id': answer_id})
    return render(request, 'lawyered/comment.html', {'answer_id': answer_id})


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        question.views += 1
        question.save()
        answer_list = question.answer_set.order_by('-votes')

        paginator = Paginator(answer_list, 10)
        page = request.GET.get('page')
        try:
            answers = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            answers = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            answers = paginator.page(paginator.num_pages)

    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'lawyered/detail.html', {'answers': answers, 'question': question}, )


def answer(request, question_id):
    if request.user.is_anonymous():
        return HttpResponseRedirect("/login/")

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'lawyered/answer.html', {'question': question})

def add_answer(request):
    if request.method == 'POST':
        answer_text = request.POST['answer']
        question_id = request.POST['question']
        user_id = request.POST['user']

        question = Question.objects.get(pk=question_id)
        user_ob = User.objects.get(id=user_id)
        user = UserProfile.objects.get(user=user_ob)
        user.points += 5
        user.save()

        if answer_text.strip() == '':
            return render(request, 'lawyered/answer.html', {'question': question, 'message': 'Empty'})

        a = Answer()
        pub_date = datetime.datetime.now()
        a.answer_text = answer_text
        a.question = question
        a.user_data = user
        a.pub_date = pub_date
        a.save()

        answer_list = question.answer_set.order_by('-votes')

        paginator = Paginator(answer_list, 10)
        page = request.GET.get('page')
        try:
            answers = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            answers = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            answers = paginator.page(paginator.num_pages)

        return render(request, 'lawyered/detail.html', {'question': question, 'answers': answers})

    return render(request, 'lawyered/detail.html', {'question': question})

def vote(request, user_id, answer_id, question_id, op_code):

    user_ob = User.objects.get(id=user_id)
    user = UserProfile.objects.get(user=user_ob)
    answer = Answer.objects.get(pk=answer_id)
    question = Question.objects.get(pk=question_id)

    answer_list = question.answer_set.order_by('-votes')

    paginator = Paginator(answer_list, 10)
    page = request.GET.get('page')
    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        answers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        answers = paginator.page(paginator.num_pages)

    if Answer.objects.filter(id=answer_id, user_data=user).exists():
        return render(request, 'lawyered/detail.html', {'question': question, 'answers': answers, 'message':"You cannot vote on your answer!"})

    if Voter.objects.filter(answer_id=answer_id, user=user).exists():
        return render(request, 'lawyered/detail.html', {'question': question, 'answers': answers, 'message':"You've already cast vote on this answer!"})

    if op_code == '0':
        answer.votes += 1
        u = answer.user_data
        u.points += 10
        u.points += question.reward
        u.save()
    if op_code == '1':
        answer.votes -= 1
        u = answer.user_data
        u.points -= 10
        u.save()
    answer.save()

    answer_list = question.answer_set.order_by('-votes')

    paginator = Paginator(answer_list, 10)
    page = request.GET.get('page')
    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        answers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        answers = paginator.page(paginator.num_pages)

    v = Voter()
    v.user = user
    v.answer = answer
    v.save()

    return render(request, 'lawyered/detail.html', {'question': question, 'answers': answers})

def thumb(request, user_id, question_id, op_code):

    user_ob = User.objects.get(id=user_id)
    user = UserProfile.objects.get(user=user_ob)
    question = Question.objects.get(pk=question_id)

    answer_list = question.answer_set.order_by('-votes')

    paginator = Paginator(answer_list, 10)
    page = request.GET.get('page')
    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        answers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        answers = paginator.page(paginator.num_pages)

    if QVoter.objects.filter(question_id=question_id, user=user).exists():
        return render(request, 'lawyered/detail.html', {'question': question, 'answers': answers, 'message':"You've already cast vote on this question!"})

    if op_code == '0':
        question.reward += 5
        u = question.user_data
        u.points += 5
        u.save()
    if op_code == '1':
        question.reward -= 5
        u = question.user_data
        u.points -= 5
        u.save()
    question.save()

    answer_list = question.answer_set.order_by('-votes')

    paginator = Paginator(answer_list, 10)
    page = request.GET.get('page')
    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        answers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        answers = paginator.page(paginator.num_pages)

    v = QVoter()
    v.user = user
    v.question = question
    v.save()

    return render(request, 'lawyered/detail.html', {'question': question, 'answers': answers})

def form_list(request):
	return render(request, 'lawyered/add_cases.html')
	
def divorce(request):
	if request.method== 'POST':
	#	user_id = request.POST.get('user')
	#	user_ob = User.objects.get(id=user_id)
		form = divorcecaseForm(request.POST)
	#	user = UserProfile.objects.get(user=user_ob)

		if form.is_valid():
			
			new_case1 = form1.save(commit=False)
	#		new_case.name = user
			new_case.save()
			return render(request,'lawyered/done.html', {'username':request.user.username})
		else:
			return render(request, 'lawyered/invalid.html')

	else:
		form = divorcecaseForm()
		return render(request, 'lawyered/divorce.html', {'form': form, 'username':request.user.username})
		
def dui(request):
	if request.method== 'POST':
	#	user_id = request.POST.get('user')
	#	user_ob = User.objects.get(id=user_id)
		form = duiCaseForm(request.POST)
	#	user = UserProfile.objects.get(user=user_ob)

		if form.is_valid():
			
			new_case = form.save(commit=False)
	#		new_case.name = user
			new_case.save()
			return render(request,'lawyered/done.html', {'username':request.user.username})
		else:
			print form.errors
			return render(request, 'lawyered/invalid.html')

	else:
		form = duiCaseForm()
		return render(request, 'lawyered/dui.html', {'form': form, 'username':request.user.username})
		
def criminal(request):
	if request.method== 'POST':
	#	user_id = request.POST.get('user')
	#	user_ob = User.objects.get(id=user_id)
		form = criminalCaseForm(request.POST)
	#	user = UserProfile.objects.get(user=user_ob)

		if form.is_valid():
			
			new_case = form.save(commit=False)
	#		new_case.name = user
			new_case.save()
			return render(request,'lawyered/done.html', {'username':request.user.username})
		else:
			return render(request, 'lawyered/invalid.html')

	else:
		form = criminalCaseForm()
		return render(request, 'lawyered/criminal.html', {'form': form, 'username':request.user.username})
		
def prenup(request):
	if request.method== 'POST':
	#	user_id = request.POST.get('user')
	#	user_ob = User.objects.get(id=user_id)
		form = prenupCaseForm(request.POST)
	#	user = UserProfile.objects.get(user=user_ob)

		if form.is_valid():
			
			new_case = form.save(commit=False)
	#		new_case.name = user
			new_case.save()
			return render(request,'lawyered/done.html', {'username':request.user.username})
		else:
			return render(request, 'lawyered/invalid.html')

	else:
		form = prenupCaseForm()
		return render(request, 'lawyered/prenup.html', {'form': form, 'username':request.user.username})
		
def merger(request):
	if request.method== 'POST':
	#	user_id = request.POST.get('user')
	#	user_ob = User.objects.get(id=user_id)
		form = mergerCaseForm(request.POST)
	#	user = UserProfile.objects.get(user=user_ob)

		if form.is_valid():
			
			new_case = form.save(commit=False)
	#		new_case.name = user
			new_case.save()
			return render(request,'lawyered/done.html', {'username':request.user.username})
		else:
			return render(request, 'lawyered/invalid.html')

	else:
		form = mergerCaseForm()
		return render(request, 'lawyered/merger.html', {'form': form, 'username':request.user.username})
		
def estate(request):
	if request.method== 'POST':
	#	user_id = request.POST.get('user')
	#	user_ob = User.objects.get(id=user_id)
		form = estateCaseForm(request.POST)
	#	user = UserProfile.objects.get(user=user_ob)

		if form.is_valid():
			
			new_case = form.save(commit=False)
	#		new_case.name = user
			new_case.save()
			return render(request,'lawyered/done.html', {'username':request.user.username})
		else:
			return render(request, 'lawyered/invalid.html')

	else:
		form = estateCaseForm()
		return render(request, 'lawyered/estate.html', {'form': form, 'username':request.user.username})
		
		

	
def forumlogout(request):
    logout(request)
    return HttpResponseRedirect('/lawyered/forum')


def divcasedetail(request, divorceForm_id):
  	dcase = divorceForm.objects.get(pk=divorceForm_id)
	return render(request, 'lawyered/divcasedet.html', {'dcase':dcase,'username':request.user.username})
	
def precasedetail(request, prenupForm_id):
  	pcase = prenupForm.objects.get(pk=prenupForm_id)
	return render(request, 'lawyered/precasedet.html', {'pcase':pcase,'username':request.user.username})
	
def cricasedetail(request, criminalForm_id):
  	ccase = criminalForm.objects.get(pk=criminalForm_id)
	return render(request, 'lawyered/cricasedet.html', {'ccase':ccase,'username':request.user.username})
	
def mercasedetail(request, mergerForm_id):
  	mcase = mergerForm.objects.get(pk=mergerForm_id)
	return render(request, 'lawyered/mercasedet.html', {'mcase':mcase,'username':request.user.username})
	
def estcasedetail(request, estateForm_id):
  	ecase = estateForm.objects.get(pk=estateForm_id)
	return render(request, 'lawyered/estcasedet.html', {'ecase':ecase,'username':request.user.username})

def duicasedetail(request, duiForm_id):
  	ducase = duiForm.objects.get(pk=duiForm_id)
	return render(request, 'lawyered/duicasedet.html', {'ducase': ducase,'username':request.user.username})
	
	
