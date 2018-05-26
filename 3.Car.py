
print "If a yes/no question is asked, please answer with 'YES' or 'NO'."
car = raw_input("Do you have a car? ").upper()

if car == "YES":
    #carinsurence: how much do you spend on your car insurance every month?
    carinsurence = raw_input("How much do you spend on your car insurence every month? ")
    #roadtaxes: how much do you spend on road taxes each month?
    roadtaxes = raw_input("How much do you spend on roadtaxes each month? ")
    #anwb: do you have an anwb membership?
    anwb = raw_input("Do you have an ANWB membership? ").upper()

    if anwb == "YES":
        anwbcosts = raw_input("How much do you pay for your membership monthly? ")
    elif anwb == "NO":
        print "Ok, no ANWB membership for you."
        anwbcosts = 0
    else:
        print "I'm sorry, I don't understand -- "+anwb+" -- I can only deal with 'YES' of 'NO'."

    #parkinglicense: do you have any costs concering a parking licence? (de laatste vraag, zo nee, dan kan alles opgeteld)
    parkingpermit = raw_input("Do you have a parking permit that you pay for? ").upper()
    if parkingpermit == "YES":
        parkingpermitcosts = raw_input("How much do you pay for your parking permit monthly? ")
    elif parkingpermit == "NO":
        print "Ok, no parking permit for you."
        parkingpermitcosts = 0
    else:
        print "I'm sorry, I don't understand -- "+parkingpermit+" -- I can only deal with 'YES' or 'NO'."
    sumcar = int(carinsurence) + int(roadtaxes) + int(anwbcosts) + int(parkingpermitcosts)
    print "Your total monthly expenses on your car are: "
    print sumcar
elif car == "NO":
    print "Ok, no car for you. Thank you for saving the planet."
else:
    print "I'm sorry, I don't understand -- "+car+" -- I can only deal with YES' or 'NO'."

print "THE END"


