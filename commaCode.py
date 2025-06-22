import sys

def comma_code(input_list):
    # 1. Controleer of de input een lijst is
    if not isinstance(input_list, list):
        # Het is beter om een specifiekere uitzondering te raisen, zoals TypeError
        raise TypeError('De input moet een lijst zijn.')

    # 2. Controleer of de lijst leeg is
    if not input_list: # Pythonische manier om te controleren of een lijst leeg is
        # Het is beter om een specifiekere uitzondering te raisen, zoals ValueError
        raise ValueError('De lijst mag niet leeg zijn.')

    # 3. Verwerk de lijst en formatteer de uitvoer
    # Maak een lijst van strings voor de elementen die met komma's gescheiden worden
    formatted_items = [str(item) for item in input_list[:-1]] # Alle elementen behalve de laatste

    # Voeg het laatste element toe met 'en'
    # Controleer of er meer dan één element is om correct te formatteren
    if len(input_list) > 1:
        result = ", ".join(formatted_items) + " en " + str(input_list[-1])
    else:
        # Als er maar één element is, print dan gewoon dat element
        result = str(input_list[0])

    print(result)

# --- Deel voor gebruikersinput ---
user_list = []
print('Voer items in om een lijst te maken. Voer een lege regel in om te stoppen.')
while True:
    item = input()
    if item: # Controleer direct of de string niet leeg is
        user_list.append(item)
    else: # Als de string leeg is, stop de loop
        break

# --- Aanroepen van de functie met try-except blokken ---
try:
    comma_code(user_list)
except TypeError as e:
    print(f"Fout: {e}")
except ValueError as e:
    print(f"Fout: {e}")
except Exception as e: # Vang eventuele andere onverwachte fouten op
    print(f"Er is een onverwachte fout opgetreden: {e}")