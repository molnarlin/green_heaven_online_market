from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if color:
        if item_id in list(bag.keys()):
            if color in bag[item_id]['items_by_color'].keys():
                bag[item_id]['items_by_color'][color] += quantity
            else:
                bag[item_id]['items_by_color'][color] = quantity
        else:
            bag[item_id] = {'items_by_color': {color: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount.
    Handles both color-specific and non-color products.
    """
    quantity = int(request.POST.get('quantity'))
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if color:
        if quantity > 0:
            bag[item_id]['items_by_color'][color] = quantity
        else:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    try:
        item_id = str(item_id)
        color = request.POST.get('product_color', None)
        bag = request.session.get('bag', {})

        if color:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception:
        return HttpResponse(status=500)
