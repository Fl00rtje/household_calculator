#misschien hier vragen naar OV abonnement: trein?
ovtrain = raw_input("Do you have an OV membership for the train? ").upper()
if ovtrain == "YES":
    ovtraincosts = raw_input("How much do you pay for your membership monthly? ")
elif ovtrain == "NO":
    print "Ok, no membership for the train for you."
    ovtraincosts = 0
else:
    print "I'm sorry, I don't understand -- "+ovtrain+" -- I can only deal with 'YES' or 'NO'."

#misschien hier vragen naar OV abonnement: tram?
ovtram = raw_input("Do you have an OV membership for the tram? ").upper()
if ovtram == "YES":
    ovtramcosts = raw_input("How much do you pay for your membership monthly? ")
elif ovtram == "NO":
    print "Ok, no membership for the tram for you"
    ovtramcosts = 0
else:
    print "I'm sorry, I don't understand -- "+ovtrain+" -- I can only deal with 'YES' or 'NO'."

#misschien hier vragen naar OV abonnement: bus?
ovbus = raw_input("Do you have an OV membership for the bus? ").upper()
if ovbus == "YES":
    ovbuscosts = raw_input("How much do you pay for your membership monthly? ")
elif ovbus == "NO":
    print "Ok, no membership for the bus for you"
    ovbuscosts = 0
else:
    print "I'm sorry, I don't understand -- "+ovtrain+" -- I can only deal with 'YES' or 'NO'."

sumov = int(ovtraincosts) + int(ovtramcosts) + int(ovbuscosts)
print "Your monthly expenses on public transport are: " + str(sumov) + " euro."

#nog een totaal van de kosten van transport maken? (auto + openbaar vervoer)