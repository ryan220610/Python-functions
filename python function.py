def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def speed():
    distance = get_number("Enter distance (in meters): ")
    time = get_number("Enter time (in seconds): ")
    if time == 0:
        print("Time cannot be zero")
    else:
        print("Speed =", distance / time, "m/s")


def force():
    mass = get_number("Enter mass (in Kg): ")
    accel = get_number("Enter acceleration (in m/s²): ")
    print("Force =", mass * accel, "N")


def pressure():
    force_val = get_number("Enter force (in N): ")
    area = get_number("Enter area (in m²): ")
    if area == 0:
        print("Area cannot be zero.")
    else:
        print("Pressure =", force_val / area, "Pa")


def ohms_law():
    current = get_number("Enter current (in A): ")
    resistance = get_number("Enter resistance (in Ω): ")
    print("Voltage =", current * resistance, "V")


def work():
    force_val = get_number("Enter force (in N): ")
    distance = get_number("Enter distance (in meters): ")
    print("Work =", force_val * distance, "J")


operations = {
    "A": speed,
    "B": force,
    "C": pressure,
    "D": ohms_law,
    "E": work,
}


def show_menu():
    print("\nSelect a Physics formula")
    print("A. Speed (v = d/t)")
    print("B. Force (F = m * a)")
    print("C. Pressure (P = F / A)")
    print("D. Ohm's Law (V = I * R)")
    print("E. Work (W = F * d)")


while True:
    show_menu()
    user_choice = input("Enter a letter A-E: ").strip().upper()

    if user_choice in operations:
        operations[user_choice]()
    else:
        print("Invalid choice. Please choose from A to E.")
        continue

    again = input("\nDo you want to run another operation? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break
