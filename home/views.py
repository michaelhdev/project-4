from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from bugs.models import Bug
from features.models import Feature


def get_homepage(request):
    """This view gets the data needed to render the index.html page"""
    
    bugs_pending = Bug.objects.filter(status='pending').count() 
    bugs_inProgress = Bug.objects.filter(status='progressed').count()
    bugs_Completed = Bug.objects.filter(status='completed').count()
    total_bugs = bugs_Completed + bugs_inProgress + bugs_pending
    
    features_pending = Feature.objects.filter(status='pending').count() 
    features_inProgress = Feature.objects.filter(status='progressed').count() 
    features_Completed = Feature.objects.filter(status='completed').count()
    total_features = features_Completed + features_inProgress + features_pending
    
    status={
        "bugs_pending": bugs_pending,
        "bugs_inProgress": bugs_inProgress,
        "bugs_Completed": bugs_Completed,
        "total_bugs": total_bugs,
        "features_pending": features_pending,
        "features_inProgress": features_inProgress,
        "features_Completed": features_Completed,
        "total_features": total_features
    }
    
    return render(request, "index.html", {'status': status})