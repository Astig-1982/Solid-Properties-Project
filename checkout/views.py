from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.contexts import cart_contents

import stripe 

# Create your views here.


def checkout(request):

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your shopping cart is empty.")
        return redirect(reverse('services'))

    current_cart = cart_contents(request)
    total = float(current_cart['grand_total'])
    stripe_total = round(total)
    order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I0QyBDK9nNxncrw48NUr7VaOFaXhP2PyitGBqK3GFVi9cxRLyg73ycKNXq3KKgOLeoSUuY8xGv5kgo1Tqjd1ThW00k5svl8xl',
        'client_secret': 'test client secret',
        'stripe_total': stripe_total,
    }

    return render(request, 'checkout/checkout.html', context)
