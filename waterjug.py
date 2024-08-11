def water_jug_problem(x, y, z):
    jug1, jug2 = 0, 0  

    print(f"Goal: Measure exactly {z} liters using two jugs with capacities {x} and {y}.")
    print("\nOptions:")
    print("1. Fill Jug 1")
    print("2. Fill Jug 2")
    print("3. Empty Jug 1")
    print("4. Empty Jug 2")
    print("5. Pour Jug 1 into Jug 2")
    print("6. Pour Jug 2 into Jug 1")
    
    while jug1 != z and jug2 != z:
        print(f"\nJug 1: {jug1}/{x} liters, Jug 2: {jug2}/{y} liters")
        choice = int(input("Choose an action (1-6): "))
        
        if choice == 1:
            jug1 = x
        elif choice == 2:
            jug2 = y
        elif choice == 3:
            jug1 = 0
        elif choice == 4:
            jug2 = 0
        elif choice == 5:
            jug2 += jug1
            jug1 = 0 if jug2 <= y else jug2 - y
            jug2 = min(jug2, y)
        elif choice == 6:
            jug1 += jug2
            jug2 = 0 if jug1 <= x else jug1 - x
            jug1 = min(jug1, x)
        else:
            print("Invalid choice. Please try again.")
    print(f"\nJug 1: {jug1}/{x} liters, Jug 2: {jug2}/{y} liters")
    print(f"Congratulations! You've measured exactly {z} liters.")

x = int(input("Enter the capacity of Jug 1: "))
y = int(input("Enter the capacity of Jug 2: "))
z = int(input("Enter the target amount of water to measure: "))
water_jug_problem(x, y, z)
