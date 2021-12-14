# Write a loop that prompts the user to enter a
# series of pizza toppings until they enter a "quit"
# value. As they enter each topping, print a message
# saying that you will add that topping to their pizza.
prompt = "\nPlease enter the toppings that you wish to " \
         "add to your pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)
    # print(topping)

    if topping == 'quit':
        break
    else:
        print(f"I have added {topping} to your pizza for "
              f"you.")
