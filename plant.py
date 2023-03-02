import datetime
current_date = datetime.datetime.today()

# Define a dictionary of plants and their watering needs
plants = {'pothos': 7, 'zzplant': 14, 'finger cactus': 10, 'rosemary': 7, 'thyme': 7, 'lemon tree': 14}

while True:
    # Ask the user what plant they want to check on
    plant = input(
        "What plant would you like to check on? (pothos, zzplant, finger cactus, rosemary, thyme, lemon tree) ")

    # Check if the selected plant is in the dictionary
    if plant in plants:
        # Ask the user when they last watered the plant
        last_watered = input("When did you last water your {}? (YYYY-MM-DD) ".format(plant))
        # Calculate the time difference between the last watering and today
        days_since_watered = (datetime.date.today() - datetime.date.fromisoformat(last_watered)).days
        # Check if the plant needs watering
        if days_since_watered >= plants[plant]:
            print("It's time to water your {}!".format(plant))
        else:
            days_to_wait = plants[plant] - days_since_watered
            print("You don't need to water your {} yet. Wait {} more day(s) before watering again.".format(plant,
                                                                                                           days_to_wait))
    else:
        print("This is not the plant you are looking for.")

    # Ask if the user wants to check another plant
    answer = input("Do you want to check on another plant? (yes/no) ")
    if answer.lower() == "no":
        print("Have a good day!")
        break


