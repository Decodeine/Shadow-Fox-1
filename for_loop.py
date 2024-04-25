import random

count_six = 0
count_one = 0
count_double_six = 0

# A for loop to Simulate rolling a six-sided dice 20 times
for i in range(20):
    
    dice_roll_1 = random.randint(1, 6)
    dice_roll_2 = random.randint(1, 6)

    # Check if the current roll is a six
    if dice_roll_1 == 6:
        count_six += 1

    # Check if the current roll is a one
    if dice_roll_1 == 1:
        count_one += 1

    # Check if both rolls are sixes 
    if dice_roll_1 == 6 and dice_roll_2 == 6:
        count_double_six += 1

   

# Print the counts
print("Number of sixes rolled:", count_six)
print("Number of ones rolled:", count_one)
print("Number of times two sixes were rolled in a single roll:", count_double_six)

#A program that helps perform 10 jumping jacks at a time, towards  100 jumping jacks
def perform_jumping_jacks(total_reps):
    for i in range(total_reps):
        if (i + 1) % 10 == 0:  # Check after every 10 jumping jacks
            tired = input("Are you tired? (yes/no or y/n): ").lower()
            if tired in ["yes", "y"]:
                skip_remaining = input("Do you want to skip the remaining jumping jacks? (yes/no or y/n): ").lower()
                if skip_remaining in ["yes", "y"]:
                    print("You decided to skip the remaining jumping jacks.")
                    print("You completed a total of", i + 1, "jumping jacks.")
                    return
                else:
                    remaining_reps = total_reps - (i + 1)
                    print("You have", remaining_reps, "jumping jacks left.")
            else:
                remaining_reps = total_reps - (i + 1)
                print("You have", remaining_reps, "jumping jacks left.")
        print("Jumping jack", i + 1)
    print("You completed 100 jumping jacks!")


perform_jumping_jacks(100)

