from os import system
from tabulate import tabulate
import random
import csv

name = ""

def main():
    global name
    system("clear")
    name = input("What's your name? ")
    system("clear")
    while True:
        print(f"Hi {name}!\n Welcome to Mental Math Trainer App For 6th Grader!")
        print("_" * 50 + "\n")
        print("Main menu:")
        print("1. Start Training Session")
        print("2. View Leaderboard")
        print("3. Quit")
        choice = int(input("What would you like to do? [1-3]: "))

        if choice == 1:
            system("clear")
            selected_operation = training_session_loop()
            if selected_operation:
                system("clear")
                solve_problems(selected_operation)
        elif choice == 2:
            system("clear")
            display_leaderboard()
        elif choice == 3:
            system("clear")
            break
        else:
            system("clear")
            print("Invalid Option\n")


def training_session_loop():
    operation_categories = {
        "+" : "Addition",
        "-": "Substraction",
        "*": "Multiplication",
        "/": "Division",
    }

    while True:
        print("Select an operation:")
        for i, operator in enumerate(operation_categories):
            print(f"{i + 1}. {operation_categories[operator]}")

        try:
            operation_choice = int(input(f"Enter category [1-{len(operation_categories)}]: ")) - 1
            if 0 <= operation_choice < len(operation_categories):
                selected_operation = list(operation_categories.keys())[operation_choice]
                return selected_operation
            else:
                system("clear")
                print("Invalid Option\n")
        except ValueError:
            system("clear")
            print("Invalid Option\n")


def solve_problems(selected_operation):
    global name
    num_problems = int(input("How many problems do you want? ")) # Number of problems from each session
    score = 0
    system("clear")
    for _ in range(num_problems):
        problem = get_problem(selected_operation)
        while True:
            user_answer = get_user_answer(problem)
            correct_answer = evaluate_problem(problem)

            if user_answer == correct_answer:
                score += 1
                system("clear")
                break
            else:
                system("clear")
                print("Incorrect answer, try again...\n")        
    print(f"🥳Congratulations you've completed a session with {num_problems} problem(s)🥳")
    input("Press Enter to continue...")
    system("clear")
    update_leaderboard(name, score)


def get_problem(selected_operation): # You can adjust the random integer based on student capability
    if selected_operation == "+":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    elif selected_operation == "-":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, num1)
    elif selected_operation == "*":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif selected_operation == "/":
        num2 = random.randint(1, 10)
        result = random.randint(1, 10)
        num1 = num2 * result
    problem = [num1,selected_operation, num2]
    return problem

def evaluate_problem(problem):
    num1, operator, num2 = problem
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1/num2

def get_user_answer(problem):
    num1, operator, num2 = problem
    prompt = f"{num1} {operator} {num2} = "
    user_answer = int(input(prompt))
    return user_answer

def update_leaderboard(name, score):
    with open("leaderboard.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow([name,score])


def display_leaderboard():
    table = []
    print("Leaderboard:")
    try: 
        with open("leaderboard.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table, headers='firstrow',tablefmt='grid'))
    except FileNotFoundError:
        print("No entries in the leaderboard.")
    input("Press Enter to continue...")
    system("clear")


if __name__ == "__main__":
    main()
