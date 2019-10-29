print("how many bars need recharging")
bars_to_charge = int(input())
bars_charged = 0
print("charging...")
while (bars_charged<bars_to_charge):
    bars_charged = bars_charged + 1
    print("charging", "█" * bars_charged)
print ("The battery is fully charged!")
