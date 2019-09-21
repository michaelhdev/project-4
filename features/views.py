from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Feature, CommentForFeature
from .forms import FeatureForm, CommentForFeatureForm


def get_features(request):
    """
    A view that will return a list
    of Features that were display them on the 'features.html' template
    """
    features = Feature.objects.all().order_by('-votes')
    return render(request, "features.html", {'features': features})


def feature_detail(request, pk):
    """
    A view that returns a single
    feature object based on the feature ID (pk) and
    render it to the 'featuredetail.html' template.
    Or return a 404 error if the feature is
    not found
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
            return redirect('feature_detail', pk)
        else:
            featureCommentForm = CommentForFeatureForm()
    else:
        featureCommentForm = CommentForFeatureForm()
        
    return render(request, "featureDetail.html", {'feature': feature, 'comments' : featureComments, 'commentForm': featureCommentForm})

"""def vote_feature_up(request, pk):
    
    A view that returns a single
    feature object based on the feature ID (pk) and
    render it to the 'featuredetail.html' template.
    Or return a 404 error if the feature is
    not found
   
    feature = get_object_or_404(Feature, pk=pk)
    feature.votes += 1
    feature.save()
    return redirect(get_features) """
    
def vote_feature(request, pk):
    """
    A view that returns a single
    feature object based on the feature ID (pk) and
    render it to the 'featuredetail.html' template.
    Or return a 404 error if the feature is
    not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    user = request.user
    if user in feature.votes.all():
        feature.votes.remove(user)
    else:
        feature.votes.add(user)
    
    return redirect(get_features)
    
def create_or_edit_feature(request, pk=None):
    """
    A view that allows us to create
    or edit a feature depending if the feature ID
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
    
def sort_features(request):
    
    selection = request.GET['sort_by']
    
    features = Feature.objects.all().order_by(selection)
        
    return render(request, "features.html", {'features': features})
    
    
    
