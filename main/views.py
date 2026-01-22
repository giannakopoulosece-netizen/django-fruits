from django.shortcuts import render
from django.http import HttpResponse

# --------------------
# Αρχική σελίδα
# --------------------
def home(request):
    user_name = ""
    if request.method == "POST":
        user_name = request.POST.get("name", "").strip()
        # Πηγαίνουμε στο page με το όνομα
        return render(request, 'main/page.html', {
            'title': 'Σελίδα Φρούτων',
            'message': f'Καλώς ήρθες, {user_name}! Διάλεξε ένα φρούτο για να δεις την εικόνα του.',
            'items': [
                {'key': 'apple', 'name': 'Μήλο', 'emoji': '🍎'},
                {'key': 'orange', 'name': 'Πορτοκάλι', 'emoji': '🍊'},
                {'key': 'banana', 'name': 'Μπανάνα', 'emoji': '🍌'}
            ]
        })

    return render(request, 'main/home.html')  # GET request, απλή φόρμα

# --------------------
# Σελίδα φρούτων (page)
# --------------------
def page(request):
    # Αν θέλεις να πας απευθείας στη σελίδα χωρίς όνομα, μπορείς να έχεις default μήνυμα
    return render(request, 'main/page.html', {
        'title': 'Σελίδα Φρούτων',
        'message': 'Διάλεξε ένα φρούτο για να δεις την εικόνα του!',
        'items': [
            {'key': 'apple', 'name': 'Μήλο', 'emoji': '🍎'},
            {'key': 'orange', 'name': 'Πορτοκάλι', 'emoji': '🍊'},
            {'key': 'banana', 'name': 'Μπανάνα', 'emoji': '🍌'}
        ]
    })

# --------------------
# Σελίδα εικόνας φρούτου
# --------------------
def fruit_detail(request, name):
    fruits = {
        'apple': {
            'title': 'Μήλο',
            'image': 'main/apple.jpg'
        },
        'banana': {
            'title': 'Μπανάνα',
            'image': 'main/banana.jpg'
        },
        'orange': {
            'title': 'Πορτοκάλι',
            'image': 'main/orange.jpg'
        }
    }

    fruit = fruits.get(name)

    if not fruit:
        return HttpResponse("Φρούτο δεν βρέθηκε 😢")

    return render(request, 'main/fruit.html', fruit)

# --- Τέλος αρχείου views.py ---
