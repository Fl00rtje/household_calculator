#Betaal je elke maand voor je hypotheek, of huur? Kies "huur" of "hypotheek".
#Hypotheek: Ok, je hebt een hypotheek. Hoeveel betaal je daar per maand voor?

#Huur: Ok, je betaalt huur. Hoeveel kale huur betaal je per maand?
rent = raw_input("What is the monthly amount you pay for your basic rent/morgage? ")
servicecosts = raw_input("What is the monthly amount you pay for service costs? ")

sumrent = int(rent) + int(servicecosts)

print "So, your total expenses on rent are: " + str(sumrent) + " euro."

gas_electricity = raw_input("What is the monthly amount that you pay for gas and electricity? ")
water = raw_input("What is the monthly amount that you pay for water? ")

sum_gas_electricity_water = int(gas_electricity) + int(water)

print "Your total expenses on gas, light and water are: " + str(sum_gas_electricity_water) + " euro."

tv_internet = raw_input("What is the monthly amount that you pay for tv & internet? ")

sum_tv_internet = int(tv_internet)

print "Your total expenses on tv and internet are: " + str(sum_tv_internet) + " euro."

print "To sum up everything!"
print "Your basic rent, without utilities, is: " + str(sumrent) + " euro."
print "Your rent, including utilities like gas, electricity and water, is: " + str(sumrent + sum_gas_electricity_water) + " euro."
print "Your rent, including utilities and tv, internet is: " + str(sumrent + sum_gas_electricity_water + sum_tv_internet) + " euro."

#huur/hypotheek - check!
#service costs - check!
#gas - check!
#water - check!
#licht - check!
#internet - check!
#televisie - check!
