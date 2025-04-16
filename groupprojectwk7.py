# Initialize global variables
weeks = 0
total_days = 0
total_steps = 0

# Main function to call all other functions
def main():
    input_weeks()  # Get the number of weeks
    data_collect() # Collect the daily data
    results()  # Display the results

# Function to get the number of weeks from the user
def input_weeks():
    global weeks
    print(f"\n=== DAILY STEP TRACKER ===")
    weeks = int(input("Enter the number of weeks: "))

# Function to collect steps data
def data_collect():
    global total_days, total_steps
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday"]

    # Loop through each week
    for week in range(1, weeks + 1):
        print(f"\nFor Week {week}:")

        # Loop through each day of the week
        for day in days:
            total_days = float(input(f"Enter steps for day {day}: "))
            total_steps += total_days
            total_days += 1

# Function to perform the calculations
def calculations():
    global total_steps, total_days
    average_steps = total_steps / total_days if total_days != 0 else 0
    return average_steps

# Function to display the results
def results():
    global total_steps, total_days
    print("\nResults:")
    print(f"In {total_days:,.0f} days:")
    print(f"Total steps: {total_steps:,.0f} steps")
    print(f"Average steps per day: {calculations():,.0f} steps")

# Run the main function
main()