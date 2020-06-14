#Ground Shipping Cost
def ground_shipping(weight):

  flat_charge = 20

  if (weight <= 2):
    cost = 1.5 * weight + flat_charge
  elif (weight > 2) and (weight <= 6):
    cost = 3 * weight + flat_charge
  elif (weight > 6) and (weight <= 10):
    cost = 4 * weight + flat_charge
  else:
    cost = 4.75 * weight + flat_charge

  return cost

print(ground_shipping(8.4))

#Premium Shipping Cost
premium_shipping_cost = 125

#Drone Shipping Cost
def drone_shipping(weight):

  flat_charge = 0

  if (weight <= 2):
    cost = 4.5 * weight + flat_charge
  elif (weight > 2) and (weight <= 6):
    cost = 9 * weight + flat_charge
  elif (weight > 6) and (weight <= 10):
    cost = 12 * weight + flat_charge
  else:
    cost = 14.25 * weight + flat_charge

  return cost

print(drone_shipping(1.5))

#Cheapest Shipping Cost
def cheapest_shipping(weight):

  if(ground_shipping(weight) < drone_shipping(weight)) and (ground_shipping(weight) < premium_shipping_cost):
    return ground_shipping(weight)
  elif (drone_shipping(weight) < ground_shipping(weight)) and (drone_shipping(weight) < premium_shipping_cost):
    return drone_shipping(weight)
  else:
    return premium_shipping_cost

print(cheapest_shipping(4.8))
