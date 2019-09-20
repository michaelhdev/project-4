from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bug, CommentForBug
from .forms import BugForm, CommentForBugForm


def get_bugs(request):
    """
    A view that will return a list
    of Bugs that were display them on the 'bugs.html' template
    """
    bugs = Bug.objects.all().order_by('status')
    return render(request, "bugs.html", {'bugs': bugs})


def bug_detail(request, pk):
    """
    A view that returns a single
    bug object based on the bug ID (pk) and
    render it to the 'bugdetail.html' template.
    Or return a 404 error if the bug is
    not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    return render(request, "bugDetail.html", {'bug': bug})


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
            bug = form.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugForm.html', {'form': form})
    
    
    
    