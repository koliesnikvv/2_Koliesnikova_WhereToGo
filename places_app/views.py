from django.shortcuts import render, redirect, get_object_or_404
import random
from .models import Place
from .forms import PlaceForm

def home(request):
    random_place = None

    if request.method == 'GET' and 'randomize' in request.GET:
        places = list(Place.objects.all())
        if places:
            weights = [place.rating ** 2 for place in places]
            random_place = random.choices(places, weights=weights, k=1)[0]

    return render(request, 'home.html', {'random_place': random_place})

def places_list(request):
    places = Place.objects.all().order_by('-created_at')
    return render(request, 'places/place_list.html', {'places': places})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'places/place_detail.html', {'place': place})

def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('places_list')
    else:
        form = PlaceForm()
    return render(request, 'places/place_form.html', {'form': form})