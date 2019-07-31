import functions

public_transport = functions.yes_or_no("Do you have a public transport membership f.e. for bus, tram or train?")

def cost_membership_bus():
    amount = 0
    if functions.yes_or_no("Do you pay for a bus membership?"):
        amount = functions.ask_amount("How much do you pay for your bus membership? € ")
    return amount

def cost_membership_tram():
    amount = 0
    if functions.yes_or_no("Do you pay for a tram membership?"):
        amount = functions.ask_amount("How much do you pay for your tram membership? € ")
    return amount

def cost_membership_train():
    amount = 0
    if functions.yes_or_no("Do you pay for a train membership?"):
        amount = functions.ask_amount("How much do you pay for your train membership? € ")
    return amount

if public_transport:
    bus_costs = cost_membership_bus()
    tram_costs = cost_membership_tram()
    train_costs = cost_membership_train()
    total_public_transport = bus_costs + tram_costs + train_costs
    print(f'The total amount you are spending on public transport is € {total_public_transport}')
else:
    print("Please consider using public transport. It helps save the planet.")
    print("Unless your walking or biking. Then you're cool.")

