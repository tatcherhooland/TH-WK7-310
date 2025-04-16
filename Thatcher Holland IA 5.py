# This initializes the global variables so they can be called in functions
years = 0
total_rainfall = 0
total_months = 0
average_rainfall = 0

# This is the main function used to call all other functions
def main():
    input_years()  # This function sets the number of years from the user
    data_collect() # This function collects the monthly data for each year
    calculations() # This function calculates the average rainfall
    results()      # This function displays the results

# Define what's a part of this function
def input_years():
    # Use the global years variable
    global years
    # Tell the user what the program does with an f string
    print(f"\n=== AVERAGE RAINFALL CALCULATOR ===")
    # Prompt user to input how many years they need data for, which is handled as an integer
    years = int(input("Enter the number of years: "))

# Define what's a part of this function
def data_collect():
    # Use the global total_rainfall and total_months variables
    global total_rainfall, total_months
    # Sets up an array for every month in the year
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    # Loop through each year that the user needs data for
    for year in range(1, years + 1):
        # Display which year the user is inputting data for with an f string
        print(f"\nFor Year {year}:")

        # Loop through each month of the year that the user needs data for
        for month in months:
            # Prompt user to input how many inches of rainfall they need data for that month
            # This is handled as a float
            rainfall = float(input(f"Enter the inches of rainfall for {month}: "))
            # Add that month's rainfall to the total rainfall unless the entry is negative
            # Default a negative rainfall entry to 0 to avoid skewing data
            total_rainfall += rainfall if rainfall >= 0 else 0
            # Add a month to the total monthly count
            total_months += 1

# Define what's a part of this function
def calculations():
    # Use the global total_rainfall, total_months, and average_rainfall variables
    global total_rainfall, total_months, average_rainfall
    # Divide the total rainfall by the total months to calculate the average rainfall
    # Default the average rainfall to 0 if the total months are 0 (Caused by user inputting 0 years)
    # This is to avoid an error through trying to divide by 0
    average_rainfall = total_rainfall / total_months if total_months != 0 else 0

# Define what's a part of this function
def results():
    # Use the global total_rainfall, total_months, and average_rainfall variables
    global total_rainfall, total_months, average_rainfall
    # Display a header with an f string
    print("\nResults:")
    # Display the total months with an f string
    print(f"For {total_months} months:")
    # Display the total rainfall across all months with an f string to two decimal places
    print(f"Total rainfall: {total_rainfall:,.2f} inches")
    # Display the average monthly rainfall with an f string to two decimal places
    print(f"Average monthly rainfall: {average_rainfall:,.2f} inches")

# Run the main function
main()