massa = float(input("Введи массу конфет в граммах: ")) 

if massa > 2000: 
    chena = massa / 1000 * 200 
    print(f"200 руб за 1 кг, Итого: {chena} руб") 
else: 
    chena = massa / 1000 * 250 
    print(f"250 руб за 1 кг, Итого: {chena} руб")
