from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if color:
        if item_id in bag:
            if 'items_by_color' not in bag[item_id]:
                bag[item_id]['items_by_color'] = {}
            if color in bag[item_id]['items_by_color']:
                bag[item_id]['items_by_color'][color] += quantity
            else:
                bag[item_id]['items_by_color'][color] = quantity
        else:
            bag[item_id] = {'items_by_color': {color: quantity}}

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount.
    Handles both color-specific and non-color products.
    """
    quantity = int(request.POST.get('quantity'))
    color = request.POST.get('product_color', None)
    bag = request.session.get('bag', {})

    if color:
        # Ensure the item and color exist before modifying
        if item_id in bag:
            if 'items_by_color' not in bag[item_id]:
                bag[item_id]['items_by_color'] = {}

            if quantity > 0:
                bag[item_id]['items_by_color'][color] = quantity
            else:
                bag[item_id]['items_by_color'].pop(color, None)
                if not bag[item_id]['items_by_color']:
                    bag.pop(item_id)
        else:
            if quantity > 0:
                bag[item_id] = {'items_by_color': {color: quantity}}
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id, None)

    request.session['bag'] = bag
    return redirect('view_bag')


def remove_from_bag(request, item_id):
    try:
        color = request.POST.get('product_color', None)
        bag = request.session.get('bag', {})

        if color:
            if item_id in bag and 'items_by_color' in bag[item_id]:
                bag[item_id]['items_by_color'].pop(color, None)
                if not bag[item_id]['items_by_color']:
                    bag.pop(item_id, None)
        else:
            bag.pop(item_id, None)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        print(
            f"Error removing item from bag: {e}"
        )  # Optional: log for debugging
        return HttpResponse(status=500)
