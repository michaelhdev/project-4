from django.shortcuts import render, redirect, reverse

def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def delete_from_cart(request, id):
    """
    Deletes the donation from the cart
    """
    cart = request.session.get('cart', {})

    cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))