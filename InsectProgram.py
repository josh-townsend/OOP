import InsectClass as i


mosquito = i.Insect(2,4,'mosquito')
housefly = i.Insect(2,4,'housefly')

mosquito.calc_flight()
housefly.calc_flight()

print(f"{mosquito.get_name()} can fly up to {mosquito.get_miles()} miles.")
print(f"{housefly.get_name()} can fly up to {housefly.get_miles()} miles.")