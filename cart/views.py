from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

@login_required
def add_to_cart(request, id):
    """Add a donation for a feature to the cart"""
    
    donation = int(request.POST.get('donation'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = cart[id] + donation
    else:
        cart[id] = cart.get(id, donation)

    request.session['cart'] = cart
    messages.success(request, f'Donation added, ready for checkout')
    return redirect(reverse('get_features'))

@login_required
def delete_from_cart(request, id):
    """
    Deletes the donation from the cart
    """
    cart = request.session.get('cart', {})

    cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))