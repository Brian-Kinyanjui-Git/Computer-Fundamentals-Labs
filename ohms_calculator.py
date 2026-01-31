
while True:
    print("\n--- New Calculation ---")


    user_input = input("Press Enter to continue or type 'exit' to stop: ")
    if user_input == 'exit':
        break  # stops the loop

    try:
        voltage = float(input("Enter Voltage (V): "))
        resistance = float(input("Enter Resistance (Ohms): "))


        if resistance == 0:
            print("Error: Resistance cannot be zero.")
        else:

            current = voltage / resistance
            power = voltage * current

            print("Current:", current, "Amps")
            print("Power:", power, "Watts")

    except ValueError:
        print("Error: Please enter numbers only!")