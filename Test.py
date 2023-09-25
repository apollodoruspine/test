#Zuil
naam = input("Wat is uw naam? ")
if not naam:
    naam = "Anoniem"
print(f"Hallo {naam}! Wij zijn erg benieuwd naar uw mening over ons. U kunt uw opmerkingen hieronder invoeren.")

HoeveelheidKarakters = 140
while True:
    bericht = input("Voer uw bericht in (maximaal 140 karakters): ")
    if len(bericht) <= HoeveelheidKarakters:
        print("Bedankt voor het invullen van uw bericht!")
        break
    else: print("Uw bericht is te lang. Probeer het opnieuw.")

import datetime
current_date_time = datetime.datetime.now()
formatted_date_time =











