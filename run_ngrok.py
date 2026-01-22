from pyngrok import ngrok
import os

# Βήμα 1: Τρέξε το Django server σε background
os.system("python manage.py runserver &")

# Βήμα 2: Άνοιξε tunnel προς το localhost:8000
url = ngrok.connect(8000)
print("Το δημόσιο URL είναι:", url)

# Αφήνουμε το script να τρέχει για να κρατήσει το tunnel ανοιχτό
input("Πατήστε Enter για να κλείσετε το ngrok...")