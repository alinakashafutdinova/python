def calculate_candy_price():
    mass = float(input("Введите массу конфет в граммах: "))
    
    if mass > 2000:
        price = 200 * (mass / 1000)
    else:
        price = 250 * (mass / 1000)
    
    print(f"Цена конфет составит {price} рублей.")

calculate_candy_price()