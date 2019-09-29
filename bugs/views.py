from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bug, CommentForBug
from .forms import BugForm, CommentForBugForm
from django.contrib.auth.decorators import login_required

@login_required
def get_bugs(request):
    """
    A view that will return a list
    of Bugs that were display them on the 'bugs.html' template
    """
    bugs = Bug.objects.all().order_by('created_date')
    
    for bug in bugs:
        bugComments = CommentForBug.objects.filter(bug=bug)
        bug.comments = bugComments.count()
        bug.save()
        
    return render(request, "bugs.html", {'bugs': bugs})

@login_required
def bug_detail(request, pk):
    """
    A view that returns a single
    bug object based on the bug ID (pk) and
    render it to the 'bugdetail.html' template.
    Or return a 404 error if the bug is
    not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    user = request.user
    bugComments = CommentForBug.objects.filter(bug=bug)
    if request.method == 'POST':
        bugCommentForm = CommentForBugForm(request.POST)
        if bugCommentForm.is_valid():
            bugCommentForm.instance.author = user
            bugCommentForm.instance.bug = bug
            bugCommentForm.save()
            bug.comments = bug.comments + 1
            bug.save()
            return redirect('bug_detail', pk)
        else:
            bugCommentForm = CommentForBugForm()
    else:
        bugCommentForm = CommentForBugForm()
        
    return render(request, "bugDetail.html", {'bug': bug, 'comments' : bugComments, 'commentForm': bugCommentForm})

@login_required 
def vote_bug(request, pk):
    """
    A view that returns a single
    bug object based on the bug ID (pk) and
    render it to the 'bugdetail.html' template.
    Or return a 404 error if the bug is
    not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    user = request.user
    if user in bug.votes.all():
        bug.votes.remove(user)
        bug.save()
    else:
        bug.votes.add(user)
        bug.save()
    return redirect(get_bugs)

@login_required   
def create_or_edit_bug(request, pk=None):
    """
    A view that allows us to create
    or edit a bug depending if the bug ID
    is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug = form.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugForm.html', {'form': form})

@login_required
def sort_bugs(request):
    
    selection = request.GET['sort_by']
    
    bugs = Bug.objects.all().order_by(selection)
        
    return render(request, "bugs.html", {'bugs': bugs})
    
    
    