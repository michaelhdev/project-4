from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Feature, CommentForFeature
from .forms import FeatureForm, CommentForFeatureForm
from django.contrib.auth.decorators import login_required

@login_required
def get_features(request):
    """
    A view that will return a list of Features and send them to the 'features.html' template.
    It also sets up what the admin is working on by checking the top 3 donations with the status 
    of in progress. It also updates the comment count in case the admin has deleted a comment
    """
    features = Feature.objects.all().order_by('-totalDonation')
    inProgressFeatures = Feature.objects.filter(status='progressed').order_by('-totalDonation')
    index = 0
    workingOn = []
    for feature in inProgressFeatures:
        
        if index < 3:
            workingOn.insert(index,feature.title)
            index = index + 1
            
    for feature in features:
        featureComments = CommentForFeature.objects.filter(feature=feature)
        feature.comments = featureComments.count()
        feature.save()
    return render(request, "features.html", {'features': features, 'workingOn':workingOn})

@login_required
def feature_detail(request, pk):
    """
    A view that returns a single feature object based on the feature ID (pk) and
    render it to the 'featuredetail.html' template.Or return a 404 error if the feature is
    not found. If a comment is posted it saves it to the database
    """
    feature = get_object_or_404(Feature, pk=pk)
    user = request.user
    featureComments = CommentForFeature.objects.filter(feature=feature)
    if request.method == 'POST':
        featureCommentForm = CommentForFeatureForm(request.POST)
        if featureCommentForm.is_valid():
            featureCommentForm.instance.author = user
            featureCommentForm.instance.feature = feature
            featureCommentForm.save()
            feature.comments = feature.comments + 1
            feature.save()
            return redirect('feature_detail', pk)
        else:
            featureCommentForm = CommentForFeatureForm()
    else:
        featureCommentForm = CommentForFeatureForm()
        
    return render(request, "featureDetail.html", {'feature': feature, 'comments' : featureComments, 'commentForm': featureCommentForm})

    
@login_required
def create_or_edit_feature(request, pk=None):
    """
    A view that allows us to create or edit a feature depending if the feature ID
    is null or not
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature = form.save()
            return redirect(feature_detail, feature.pk)
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'featureForm.html', {'form': form})

@login_required
def sort_features(request):
    """A view that sorts features based on the users selection. 
    If donations are selected it sorts in decending order
    """
    selection = request.GET['sort_by']
    
    if selection == 'totalDonation':
       
        features = Feature.objects.all().order_by('-totalDonation')
    
    else:
        
        features = Feature.objects.all().order_by(selection)
        
    return render(request, "features.html", {'features': features})
    
    
    
