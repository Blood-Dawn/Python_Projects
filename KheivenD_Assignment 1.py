# Kheiven D'haiti
# Assignment 1
# 1/21/2025

import random 
from datetime import datetime

# Utility function to print a divider line
def print_divider(title=None):
    print("\n" + "=" * 40)  # Prints a line of 40 "=" symbols
    if title:
        print(f"--- {title} ---")  # Optional title for the section
    print("=" * 40 + "\n")

# Great Lakes Program
# Plan and Steps:
# Calculate the depth using the formula: depth = volume / area
# Convert the depth from kilometers to meters
# Write test cases

print_divider("Great Lakes Program")

great_lake_volume = 22810
us_area = 8080464
depth = great_lake_volume / us_area
depth_m = depth * 1000

print(f"Over that amount of area({us_area}) would be {depth:.6f} kilometers and {depth_m:.2f} meters.\n")

# Voyager 1 Program
# Plan and Steps:
# Compute the time passed in hours and calculate the additional distance traveled
# Add the initial distance to the traveled distance to get the total distance
# Convert the distance into kilometers and Astronomical Units
# Calculate the round-trip communication time in hours based on the speed of light
# Write test cases with different numbers of days to validate the calculations

print_divider("Voyager 1 Program")

def voyager_distance(days):
    initial_distance = 16637000000  
    speed_mph = 38241  
    km_miles= 1.609344
    au_miles = 92955887.6

    # Calculate total distance in miles
    hours_passed = days * 24
    traveled_distance = speed_mph * hours_passed
    total_distance = initial_distance + traveled_distance

    # Convert distances
    total_distance_km = total_distance * km_miles
    total_distance_au = total_distance / au_miles

    # Round-trip communication time
    round_trip = (total_distance * 1609.344 / 299792458) * 2 / 3600

    return total_distance, total_distance_km, total_distance_au, round_trip

days = int(input("How long has it been since 09/25/2009:"))

distance_miles, distance_km, distance_au, comm_time = voyager_distance(days)

print(f"\nIt's been {days} days since 09/25/2009:")
print(f"Distance from earth in miles: {distance_miles:.2f}")
print(f"Distance from earth in kilometers: {distance_km:.2f}")
print(f"Distance from earth in Astronomical Units (AU): {distance_au:.6f}")
print(f"It will take: {comm_time:.2f} hours to send and receive a signal from Voyager 1.")

# Convert Seconds to HH:MM:SS Format
# Plan and Steps:
# Use formula to calculate the number of hours: hours = seconds // 3600.
# Use formula to calculate the remaining seconds: minutes = remaining_seconds // 60.
# Format the result as HH:MM:SS
# Write test cases to verify the output.

print_divider("Convert Seconds to HH:MM:SS Format")

def seconds_conveter(total_seconds):
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    # Format
    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
try:
    seconds = int(input("Enter the number of seconds (1-86,400): "))
    if seconds < 1 or seconds > 86400:
        print("Seconds must be between 1 and 86,400.")
    else:
        time = seconds_conveter(seconds)
        print(f"The time is: {time}")
except ValueError:
    print("Please enter a NUMBER!, lets be smart.")

# Display Current Date and Time
# Plan and Steps:
# Use the `datetime` module to fetch the current date and time.
# display the date and time in the format MM/DD/YYYY HH:MM:SS.
# Print the formatted date and time.
# Write test cases to verify the output.

print_divider("Display Current Date and Time")
def current_datetime():
    # Get current date and time
    now = datetime.now()

    # Format date and time
    formatted_datetime = now.strftime("%m/%d/%Y at %H:%M:%S")

    # Print result
    print(f"Right now is {formatted_datetime}")

# Call the function
current_datetime()

# Chessboard Grains Calculation
# Plan and Steps:
# Use formula to compute the total grains: total_grains = 2^64 - 1
# Multiply the total grains by the weight of a single grain
# calculate the depth by dividing the total weight by the area
# Write test cases for different areas

print_divider("Chessboard Grains Calculation")
def chessboard_grains(area=None):
    total_squares = 64
    weight_per_grain = 50 * 10**-6  # 50 mg in kg

    # Total grains (sum of geometric series)
    total_grains = (2**total_squares) - 1

    # Total weight in kilograms
    total_weight = total_grains * weight_per_grain

    # Depth calculation (optional)
    if area:
        depth_meters = total_weight / area
        return total_grains, total_weight, depth_meters
    else:
        return total_grains, total_weight

area = float(input("Enter the area (in square meters) to calculate depth, or press Enter to skip: ") or 0)

if area > 0:
    grains, weight, depth = chessboard_grains(area)
    print(f"Total grains on the chessboard: {grains}")
    print(f"Total weight of grains: {weight:.2f} kg")
    print(f"Depth if spread over {area:.2f} m²: {depth:.3f} meters")
else:
    grains, weight = chessboard_grains()
    print(f"Total grains on the chessboard: {grains}")
    print(f"Total weight of grains: {weight:.2f} kg")

# Paper Folding Thickness Calculation
# Plan and Steps:
# Start with the paper's initial thickness (0.1 mm or 0.0001 meters).
# Use the formula: thickness = initial_thickness × (2^folds).
# Convert the thickness to kilometers by dividing the result by 1,000.
# Write test cases for different numbers of folds to validate the calculations.

print_divider("Paper Folding Thickness Calculation")
def paper_thickness(folds):
    initial_thickness = 0.0001
    final_thickness= initial_thickness * (2 ** folds)
    final_thickness_km = final_thickness / 1000

    return final_thickness, final_thickness_km

folds = int(input("Enter the number of folds: "))
thickness_m, thickness_km = paper_thickness(folds)

print(f"\nAfter {folds} folds:")
print(f"Thickness in meters: {thickness_m:.5f}")
print(f"Thickness in kilometers: {thickness_km:.5f}")

# Closest Number Game
# Plan and Steps:
# Make a random secret number
# Make a random number between 1 and 100
# Get guesses from two players as input
# Compute the absolute difference between each player's guess and the secret number
# Compare the differences to determine the winner. Handle ties if both players are equally close
# Write test cases 

print_divider("Closest Number Game")
def closest_number():
    try:
        secret_number = random.randint(1, 100)
        player1_guess = int(input("Player 1, enter your guess (1-100): "))
        player2_guess = int(input("Player 2, enter your guess (1-100): "))

        player1_diff = abs(secret_number - player1_guess)
        player2_diff = abs(secret_number - player2_guess)

        print(f"The secret number is: {secret_number}")
        if player1_diff < player2_diff:
            print("Player 1 is closer! Player 1 wins!")
        elif player2_diff < player1_diff:
            print("Player 2 is closer! Player 2 wins!")
        else:
            print("It's a tie! Both players are equally close.")
    except ValueError:
        print("Please enter a NUMBER!! between 1 and 100.")

# Run the game
closest_number()

# Use the `random.choice` method to randomly select the computer's choice
# Accept the user's input and validate it to ensure it's one of the valid options (rock, paper, scissors)
# Compare the user's choice and the computer's choice
# Handle ties if both choices are the same
# Write test cases 

print_divider("Rock, Paper, Scissors Game")
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if user_choice not in choices:
        print("Please select rock, paper, or scissors.")
        return
    
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("Computer wins! Machines rule agian.")

# Run the game
rock_paper_scissors()


# TEST CASES FOR ALL PROBLEMS
print_divider("Test Cases")

# 1. Great Lakes Depth Calculation
print("\n--- Test Cases: Great Lakes Program ---")
great_lake_volume = 22810
us_area_cases = [8080464, 80464, 10000000, 7500000]

# Iterate through different area test cases
for i, area in enumerate(us_area_cases, start=1):
    depth_km = great_lake_volume / area
    depth_meters = depth_km * 1000
    print(f"Test Case {i}: Area = {area}")
    print(f"Depth: {depth_km:.6f} km or {depth_meters:.2f} m\n")

# 2. Voyager 1 Program
print("\n--- Test Cases: Voyager 1 Program ---")
test_days = [0, 365, 5000]

# Iterate through different day test cases
for i, days in enumerate(test_days, start=1):
    distance_miles, distance_km, distance_au, comm_time = voyager_distance(days)
    print(f"Test Case {i}: Days = {days}")
    print(f"Distance in miles: {distance_miles:.2f} mi")
    print(f"Distance in kilometers: {distance_km:.2f} km")
    print(f"Distance in AU: {distance_au:.6f} AU")
    print(f"Round-trip communication time: {comm_time:.2f} hours\n")

# 3. Seconds to HH:MM:SS
print("\n--- Test Cases: Seconds to HH:MM:SS ---")
test_seconds = [1, 70000, 86400]

# Iterate through different seconds test cases
for i, seconds in enumerate(test_seconds, start=1):
    print(f"Test Case {i}: Seconds = {seconds}")
    print(f"Time: {seconds_conveter(seconds)}\n")

# 4. Current Date and Time
print("\n--- Test Case: Current Date and Time ---")
# Display the current date and time
current_datetime()

# 5. Chessboard Grains
print("\n--- Test Cases: Chessboard Grains ---")
test_areas = [None, 10000, 1000000]

# Iterate through different area test cases
for i, area in enumerate(test_areas, start=1):
    if area:
        grains, weight, depth = chessboard_grains(area)
        print(f"Test Case {i}: Area = {area} m²")
        print(f"Total grains: {grains}")
        print(f"Total weight: {weight:.2f} kg")
        print(f"Depth: {depth:.6f} meters\n")
    else:
        grains, weight = chessboard_grains()
        print(f"Test Case {i}: No area provided")
        print(f"Total grains: {grains}")
        print(f"Total weight: {weight:.2f} kg\n")

# 6. Paper Folding Thickness
print("\n--- Test Cases: Paper Folding ---")
test_folds = [10, 30, 50]

# Iterate through different fold test cases
for i, folds in enumerate(test_folds, start=1):
    thickness_m, thickness_km = paper_thickness(folds)
    print(f"Test Case {i}: Folds = {folds}")
    print(f"Thickness: {thickness_m:.6f} m or {thickness_km:.9f} km\n")

# 7. Closest Number Game (Simulated Inputs)
print("\n--- Test Cases: Closest Number Game ---")
test_cases = [
    {"secret": 50, "player1": 45, "player2": 60},
    {"secret": 25, "player1": 20, "player2": 30},
    {"secret": 73, "player1": 80, "player2": 65},
]

# Iterate through different game scenarios
for i, case in enumerate(test_cases, start=1):
    secret_number = case["secret"]
    player1_guess = case["player1"]
    player2_guess = case["player2"]
    player1_diff = abs(secret_number - player1_guess)
    player2_diff = abs(secret_number - player2_guess)
    print(f"Test Case {i}: Secret = {secret_number}, Player 1 = {player1_guess}, Player 2 = {player2_guess}")
    if player1_diff < player2_diff:
        print("Player 1 is closer! Player 1 wins!\n")
    elif player2_diff < player1_diff:
        print("Player 2 is closer! Player 2 wins!\n")
    else:
        print("It's a tie! Both players are equally close.\n")

# 8. Rock, Paper, Scissors (Simulated Inputs)
print("\n--- Test Cases: Rock, Paper, Scissors ---")
rps_cases = [
    {"computer": "rock", "user": "scissors"},
    {"computer": "scissors", "user": "scissors"},
    {"computer": "paper", "user": "rock"},
]

# Iterate through different game scenarios
for i, case in enumerate(rps_cases, start=1):
    computer_choice = case["computer"]
    user_choice = case["user"]
    print(f"Test Case {i}: Computer = {computer_choice}, User = {user_choice}")
    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!\n")
    else:
        print("Computer wins!\n")
