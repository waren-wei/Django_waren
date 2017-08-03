from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	"""学习主题主页"""

	return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
	"""显示所有主题"""
	topics= Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/topics.html', context)

@login_required
def topic(request,topic_id):
	"""显示单个文章的页面"""
	topic= Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context= {'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
	"""添加新主题"""
	if request.method != 'POST':
		form =TopicForm()
	else:
		form =TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context= {'form':form}
	return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
	"""添加新主题的内容"""
	topic= Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		form = EntryForm()
	else:
		form= EntryForm(data=request.POST)
		if form.is_valid():
			new_entry=form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))

	context ={'topic':topic ,'form':form}
	return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
	"""编辑既有的主题内容"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method !='POST':
		form= EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))

	context = {'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)
