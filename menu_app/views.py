from django.shortcuts import render, redirect
from menu_app.models import Drink

def drinks_list(request):
    drinks = Drink.objects.all()
    return render(request, "menu_app/menu.html", context={'drinks': drinks})

def drink_detail(request, id):
    drink = Drink.objects.get(id=id)
    return render(request, "menu_app/detail.html", context={'drink': drink})

def add_drink(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        ingredients = request.POST.get('ingredients')
        image = request.FILES.get('image')
        if name and price and ingredients:
            Drink.objects.create(name=name, price=price, ingredients=ingredients, image=image)
            return redirect('drinks_list')
    return render(request, 'menu_app/add_drink.html')