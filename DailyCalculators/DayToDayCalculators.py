def run_calculation():
    parts = int(input("Enter the parts amount: "))
    profit = parts * .45
    sum_of_pars_and_profits = parts + profit
    tax = 0.1125
    part_tax = sum_of_pars_and_profits * tax
    summ = sum_of_pars_and_profits + part_tax
    labor = int(input("Enter the labor: "))
    calibration = int(input("Enter the calibration rate: "))
    
    kit_material = str(input("Does it need a kit? (y/n): "))
    
    summ_kit_material = 0  # Initialize summ_kit_material here or else it wont know what to assign it to

    if kit_material.lower() == "y":
        kit = 20
        kit_tax = kit * 0.1125
        summ_kit_material += kit + kit_tax
    else:
        print("No kit needed.")
    
    
    print(f"Parts: ${parts}", f"\nTax: ${round(part_tax, 2)}", f"\nLabor: ${labor}", 
          f"\nCalibration: ${calibration}", f"\nKit: ${summ_kit_material}",)
    print(f"Tota: ${round(summ + labor + calibration + summ_kit_material, 2 )}")
    

def run_calculation_loop():
    while True:
        run_calculation()  # Call the run_calculation function

        response = input("Run another calculation? (yes/no): ")

        if response not in ["yes", "y"]:
            print("Exiting calculation program.")
            break  # Exit the loop

# Run the loop method
run_calculation_loop()