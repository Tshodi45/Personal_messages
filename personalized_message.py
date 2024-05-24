def personalized_message():
    # Ask the user for their name, age, and location
    name = input("Please enter your name: ")
    surname = input("Please enter your surname:")
    age = input("Please enter your age: ")
    location = input("Please enter your location: ")

    # Create a personalized message
    message = f"Hello, {name}! and your is {surname} You are {age} years old and live in {location}."

    # Print out the personalized message
    print(message)

# Run the function
if __name__ == "__main__":
    personalized_message()
