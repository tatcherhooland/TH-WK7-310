def main():
    try:
        # Get two numbers.
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))

        # Perform division
        result = num1 / num2
        print(f'{num1} divided by {num2} is {result}')

    except ValueError:
        print("There was an error: Please enter a valid integer.")

    except ZeroDivisionError:
        print("There was an error: Cannot divide by zero.")

#if there are any other exception other the ones above, use this to catch them
    #except Exception as e:
     #   print(f"An unexpected error occurred: {e}")

# Call the main function.
main()
# We can also use the following bloc of code to call the function
#if __name__ == '__main__':
    #main()