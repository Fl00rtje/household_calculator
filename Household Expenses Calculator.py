print "Welcome to Flora's Household Expenses Calculator."
print "My goal is to make your life a bit easier by helping you organize your monthly and yearly expenses."
print "Let's start!"

name = raw_input("What is your name?")

print "Hi"+name+"!"

print "Let's start by organizing the costs that are related to do with your house."

#Betaal je elke maand voor je hypotheek, of huur? Kies "huur" of "hypotheek".
#Hypotheek: Ok, je hebt een hypotheek. Hoeveel betaal je daar per maand voor?

#Huur: Ok, je betaalt huur. Hoeveel kale huur betaal je per maand?
rent = raw_input("What is the monthly amount you pay for your basic rent/morgage?")
servicecosts = raw_input("What is the montly amount you pay for service costs?")

sumrent = float(rent) + float(servicecosts)

print "So, your total expenses on rent are:"
print sumrent

car = raw_input("Do you have a car? Please answer 'YES' or 'NO'")
if car == YES:
    #carinsurence: how much do you spend on your car insurance every month?
    #roadtaxes: how much do you spend on road taxes each month?
    #anwb: do you have an anwb membership?
    #parkinglicense: do you have any costs concering a parking licence? (de laatste vraag, zo nee, dan kan alles opgeteld)
elif car == NO:
    #go to next question
else #I'm sorry, I don' understand car, I can only deal with YES or NO.

#do you have a car? Please answer with yes or no.
#if car == yes, dan de volgende vragen die samenhangen met de auto
#elif car == no, dan doorgaan naar de andere vraag
#else: I'm sorry, I only understand YES or NO

#vragen of gas en licht bij elkaar is of apart
#vragen of tv, internet en bellen samen zijn of apart

#HOUSE:
#huur/hypotheek - CHECK
#gas
#water
#licht
#internet
#televisie
#bellen

#mobiele telefoon

#CAR:
#auto ja/nee - CHECK
#verzekering - CHECK
#wegenbelasting - CHECK
#anwb - CHECK
#parkeervergunning - CHECK
# - nog iets verzinnen voor als er andere tekst dan "ja" en "nee" wordt ingevoerd, want daar loopt het nu nog op mis


#PUBLIC TRANSPORT:


#basisverzekering
#aanvullende verzekering
#reisverzekering
#annuleringsverzekering
#rechtsbijstandsverzekering

#abonnement krant
#abonnement tijdschrift
#overige abonnementen



gas = raw_input("What do you pay for gas every month?")
electricity = raw_input("What do you pay for electricity every month?")
gasandelectricity = raw_input("What are your monthly expenses on gas and electricity?")



