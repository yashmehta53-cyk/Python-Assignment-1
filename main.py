print("Welcome to the Daily Calorie Tracker!")
print("This program helps you check your total calories.\n")

meals = []
calories = []

n = int(input("How many meals did you have today? "))

for i in range(n):
    meal = input(f"Enter meal #{i+1} name: ")
    cal = float(input(f"Enter calories for {meal}: "))
    meals.append(meal)
    calories.append(cal)

total = sum(calories)
average = total / n
limit = float(input("\nEnter your daily calorie limit: "))

print("\n----- Calorie Summary -----")
for i in range(n):
    print(meals[i], ":", calories[i], "cal")

print("---------------------------")
print("Total Calories:", total)
print("Average per Meal:", round(average, 2))

if total > limit:
    print("⚠ You exceeded your daily limit!")
else:
    print(" You are within your daily limit!")