from django.shortcuts import get_object_or_404
from features.models import Feature


def cart_contents(request):
    """
    Ensures cart contents are available on every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    
    for id, donation in cart.items():
        feature = get_object_or_404(Feature, pk=id)
        total += donation
        cart_items.append({'id': id, 'donation': donation, 'feature': feature})
    
    return {'cart_items': cart_items, 'total': total}