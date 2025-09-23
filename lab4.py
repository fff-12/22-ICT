def format_price(price: float) -> str:
    return f"ціна: {price:.2f} грн"

def item_prices(store: dict) -> dict:
    while True:
        name = input("Введіть назву товару (або '-' для завершення): ").strip().lower()
        if name == "-":
            break
        if name in store:
            print("Товар вже існує. Введіть іншу назву.")
            continue
        price = float(input("Введіть ціну товару: "))
        store[name] = price 
    return store

def item_availability(store: dict) -> dict:
    availability = {}
    for item in store:
        while True:
            availability_input = input(f"Чи є {item} в наявності? (так/ні): ").strip().lower()
            if availability_input == "так":
                availability[item] = True
                break
            elif availability_input == "ні":
                availability[item] = False
                break
            else:
                print("Будь ласка, введіть 'так' або 'ні'.")
    return availability

def check_availability(products_to_check: list, availability: dict) -> bool:
    all_available = True
    for item in products_to_check:
        if item not in availability or not availability[item]:
            print(f"{item} - немає в наявності")
            all_available = False
    return all_available

def total_price(order: list, store: dict) -> str:
    total = 0
    for i in order:
        total += store[i]
    return format_price(total)

def calculate_order_price(availability: dict, store: dict):
    order = input("Введіть товари через кому: ").lower().split(",")
    order = [item.strip() for item in order]
    if check_availability(order, availability):
        ans = input("Купити чи переглянути ціну? (1/2): ").strip()
        if ans == "1":
            print(f"До сплати {total_price(order, store)}")
        elif ans == "2":
            print(f"Загальна {total_price(order, store)}")
        else:
            print("Некоректний ввід.")

def main():
    # store = item_prices({})
    # availability = item_availability(store)
    calculate_order_price(availability, store)
    
if __name__ == "__main__":
    store = {
        "хліб": 25.00,
        "молоко": 40.00,
        "масло": 75.50,
        "сир": 120.00,
        "яйця": 65.00,
        "кава": 150.00,
        "чай": 90.00,
        "цукор": 30.00,
        "сіль": 15.00,
        "макарони": 50.00
    }

    availability = {
        "хліб": True,
        "молоко": True,
        "масло": False,
        "сир": True,
        "яйця": False,
        "кава": True,
        "чай": True,
        "цукор": True,
        "сіль": True,
        "макарони": False
    }

    main()
