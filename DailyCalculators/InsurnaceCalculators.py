def insurance_calculator():
    parts = float(input("Enter the parts amount: "))
    molding = float(input("Enter the molding amount: "))
    material_kit = int(input("Enter the material kit amount: "))
    rain_sensor = float(input("Enter the rain sensor amount: "))
    clips = float(input("Enter the clips amount: "))
    tax = 0.1125
    labor = float((input("Enter the labor per hour rate: ")))
    calibration = int(input("Enter the calibration amount: "))

    tax_parts = (parts + molding + material_kit + rain_sensor +clips) * tax
    
    parts_percentage = parts * int(input("Enter the parts percentage: ")) / 100
    parts_minus_percentage = parts - parts_percentage

    labor_times_hourly_rate = labor * float((input("Enter how many hours for labor: ")))

    summ_of_all_parts = (parts_minus_percentage + molding + material_kit + rain_sensor + clips 
                        + tax_parts + labor_times_hourly_rate + calibration)
    
    print(f"\nParts: ${parts}", f"\nModling: ${molding}", f"\nMaterial Kit: ${material_kit}", 
          f"\nRain Sensor: ${rain_sensor}", f"\nClips: ${clips}", f"\nLabor: ${labor}",
          f"\nCalibration: ${calibration}", f"\nTotal: ${round(summ_of_all_parts, 2)}")
    

#insurance_calculator()
    
def insurance_calculator_loop():
    while True:
        insurance_calculator()
        response = input("Run another calculation? (yes/no): ")
        if response.lower() not in ["yes", "y"]:
            print("Exiting insurance calculation program.")
            break
# Run the loop method
insurance_calculator_loop()
# This code is a simple insurance calculator that takes user input for various parts and labor costs,
# calculates the total cost, and applies a tax rate. It also allows the user to run multiple calculations
# in a loop until they choose to exit. The code is structured to be user-friendly and provides clear output 
   