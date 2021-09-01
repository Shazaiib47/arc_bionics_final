from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are currently no bionics in your basket at the moment :(")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JV0CrEbNYUTjSrrY2shhZUliKoZqDwjoXe2n3dvaCdMGx4auA7ctb8p3xAFG4gqgUPlwHBia2ZVkMSOW76GFIlh00w1xJwN0h',
        'client_secret': 'test client secret,'
    }

    return render(request, template, context)