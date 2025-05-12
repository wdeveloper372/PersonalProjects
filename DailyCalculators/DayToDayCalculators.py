def run_calculation():
    parts = int(input("Enter the parts amount: "))
    profit = parts * 40 / 100
    sum_of_pars_and_profits = parts + profit
    tax = 11.25 / 100
    part_tax = sum_of_pars_and_profits * tax
    summ = sum_of_pars_and_profits + part_tax
    labor = int(input("Enter the labor: "))
    calibration = int(input("Enter the calibration rate: "))
    print(round(summ + labor + calibration))

def run_calculation_loop():
    while True:
        run_calculation()  # Call the run_calculation function

        response = input("Run another calculation? (yes/no): ")

        if response not in ['yes', 'y']:
            print("Exiting calculation program.")
            break  # Exit the loop

# Run the loop method
run_calculation_loop()