from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.
def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        Consume.objects.create(user = user, food_consumed=consume)
        '''consume = Consume(user = user, food_consumed=consume)
        consume.save()'''

    foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user = request.user)
    carbs = 0
    protein = 0
    fats = 0
    calories = 0
    
  

    for i in consumed_food:
        carbs = carbs + i.food_consumed.carbs
        protein = protein + i.food_consumed.protein
        fats = fats + i.food_consumed.fats
        calories = calories + i.food_consumed.calories

    
    

    total = {
        'carbs' : carbs,
        'protein' : protein,
        'fats' : fats,
        'calories' : calories,
    }    
    context = {'foods' : foods, 'consumed_food' : consumed_food, 'total': total }
    
    return render(request, 'myapp/index.html', context)


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)

    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    
    return render(request, 'myapp/delete.html')