def decimeters_to_meters(decimeters):
    meters = decimeters / 10
    return meters

decimeters = float(input("Введите количество дециметров: "))
meters = decimeters_to_meters(decimeters)
print(f"{decimeters} дециметров = {meters} метров")