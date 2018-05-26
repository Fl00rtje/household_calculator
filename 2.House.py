#Betaal je elke maand voor je hypotheek, of huur? Kies "huur" of "hypotheek".
#Hypotheek: Ok, je hebt een hypotheek. Hoeveel betaal je daar per maand voor?

#Huur: Ok, je betaalt huur. Hoeveel kale huur betaal je per maand?
rent = raw_input("What is the monthly amount you pay for your basic rent/morgage? ")
servicecosts = raw_input("What is the monthly amount you pay for service costs? ")

sumrent = int(rent) + int(servicecosts)

print "So, your total expenses on rent are:"
print sumrent

#nog proberen sumrent achter de dubbele punt te krijgen, dat geeft nu een error
#en een eurotekentje erbij! :)



#huur/hypotheek - check
#gas
#water
#licht
#internet
#televisie
#bellen