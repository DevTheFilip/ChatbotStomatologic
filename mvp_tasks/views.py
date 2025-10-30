from django.shortcuts import render, redirect
from django.utils import timezone
import random

# In-memory conversation store
conversation = []

# Predefined bot (patient) responses
PATIENT_RESPONSES = [
    "Bună ziua, domnule doctor! Am dureri la o măsea de jos.",
    "Mă doare atunci când mănânc ceva rece sau dulce.",
    "Da, gingia este puțin umflată.",
    "Durerea a început acum două zile.",
    "Nu am mai avut probleme stomatologice recente.",
    "Da, am luat un calmant, dar încă mă doare.",
    "Dacă apăs pe măsea, doare mai tare.",
    "Da, pot veni mâine la cabinet.",
    "Mulțumesc, domnule doctor!"
]

def get_patient_reply():
    return random.choice(PATIENT_RESPONSES)

def chat(request):
    global conversation
    if request.method == 'POST':
        message = request.POST.get('message', '').strip()
        if message:
            conversation.append({
                'sender': 'doctor',
                'text': message,
                'timestamp': timezone.now(),
            })
            bot_reply = get_patient_reply()
            conversation.append({
                'sender': 'patient',
                'text': bot_reply,
                'timestamp': timezone.now(),
            })
        return redirect('chat')
    return render(request, 'chat.html', {'conversation': conversation})

def clear_chat(request):
    global conversation
    conversation = []
    return redirect('chat')
