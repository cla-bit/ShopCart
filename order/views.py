from django.shortcuts import render
from .forms import OrderForm
from .models import OrderItem
from cart.cart import Cart
from shop.forms import SubscribeForm

# Create your views here.


def order_create(request):
    cart = Cart(request)
    subscribe = SubscribeForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'],
                    price=item['price'], quantity=item['quantity']
                )
            cart.clear()
            context = {'order': order}
            return render(request, "order_done.html", context)
    else:
        form = OrderForm()
    context = {'form': form, 'cart': cart, 'subscribe_form': subscribe}
    return render(request, "order_create.html", context)
