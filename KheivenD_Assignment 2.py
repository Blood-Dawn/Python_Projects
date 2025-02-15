"""""
 Assignment 2
 Kheiven D'Haiti
 2/14/2025

"""""

import os
import statistics
from collections import Counter

print("\n# ===========================================")
print("# Question 1: Log File Analyzer")
print("# ===========================================")

def analyze_log_file(filename):
    """
    Reads a log file, extracts error messages, counts occurrences, 
    and displays the top 3 most common errors.
    """
    try:
        with open("c:/Users/kheiv/OneDrive/Documents/School/logfile.txt", "r") as file:
            error_counts = Counter()
            for line in file:
                if "ERROR" in line:
                    error_message = line.split("ERROR", 1)[1].strip()
                    error_counts[error_message] += 1

        top_errors = error_counts.most_common(3)
        print("\nTop 3 Errors in Log File:")
        for error, count in top_errors:
            print(f"{error}: {count} occurrences")

    except FileNotFoundError:
        print("Error: The specified log file does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

analyze_log_file("logfile.txt")

print("\n# ===========================================")
print("Question 2: Dynamic Exception Handling")
print("# ===========================================")

def evaluate_expression():
    """
    Takes a mathematical expression from the user and evaluates it.
    Handles division by zero and invalid syntax.
    """
    try:
        user_input = input("Enter a mathematical expression: ")
        result = eval(user_input)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except SyntaxError:
        print("Error: Invalid syntax. Please enter a valid mathematical expression.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

evaluate_expression()

print("\n# ===========================================")
print("Question 3: File Merging and Sorting")
print("# ===========================================")

def merge_and_sort_files(file1, file2, output_file):
    """
    Reads two files containing numbers, merges their contents, sorts them,
    and writes the sorted list to an output file.
    """
    try:
        numbers = []
        with open("c:\\Users\\kheiv\\OneDrive\\Documents\\School\\test1.txt", "r") as f1:
            for line in f1:
                numbers.append(int(line.strip()))

        with open("c:\\Users\\kheiv\\OneDrive\\Documents\\School\\test2.txt", "r") as f2:
            for line in f2:
                numbers.append(int(line.strip()))

        numbers.sort()

        with open(output_file, "w") as out:
            for num in numbers:
                out.write(str(num) + "\n")

        print(f"Sorted numbers saved to {output_file}")

    except FileNotFoundError:
        print("Error: One or both input files do not exist.")
    except ValueError:
        print("Error: One of the files contains non-numeric data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

merge_and_sort_files("file1.txt", "file2.txt", "merged_sorted.txt")

print("\n# ===========================================")
print("Question 4: Handling Complex Nested Data")
print("# ===========================================")

def process_student_scores():
    """
    Processes a list of students with names, ages, and test scores.
    Calculates the average score for each student and sorts them in descending order.
    """
    students = [
        ("Alice", 20, [85, 90, 78]),
        ("Bob", 22, [88, 76, 95]),
        ("Charlie", 21, [92, 89, 85]),
        ("David", 23, [70, 80, 75])
    ]

    student_averages = []
    for name, age, scores in students:
        average_score = sum(scores) / len(scores) if scores else 0
        student_averages.append((name, average_score))

    student_averages.sort(key=lambda x: x[1], reverse=True)

    print("\nStudents sorted by highest average score:")
    for name, avg in student_averages:
        print(f"{name}: {avg:.2f}")

    top_student = student_averages[0]
    print(f"\nTop Student: {top_student[0]} with an average score of {top_student[1]:.2f}")

process_student_scores()

print("\n# ===========================================")
print("Question 5: Enhanced List Operations")
print("# ===========================================")

def process_numbers():
    """
    Takes a list of numbers from the user and calculates sum, product, median, and mode.
    Handles cases where mode does not exist.
    """
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]

    if not numbers:
        print("Error: The list is empty.")
        return

    total_sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num

    median = statistics.median(numbers)

    try:
        mode = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode = "No mode (all values unique)"

    print(f"\nSum: {total_sum}")
    print(f"Product: {product}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

process_numbers()

print("\n# ===========================================")
print("Question 6: Multi-File Search and Replace")
print("# ===========================================")

def search_and_replace(directory, search_str, replace_str):
    """
    Searches for a string in all .txt files within a directory and replaces it with a new string.
    """
    try:
        if not os.path.isdir(directory):
            print("Error: Directory does not exist.")
            return

        txt_files = [f for f in os.listdir(directory) if f.endswith(".txt")]

        if not txt_files:
            print("No .txt files found in the directory.")
            return

        for filename in txt_files:
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                content = file.read()

            modified_content = content.replace(search_str, replace_str)

            with open(file_path, "w") as file:
                file.write(modified_content)

            print(f"Replaced occurrences in: {filename}")

    except PermissionError:
        print("Error: Insufficient permissions to modify files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

search_and_replace("C:/Users/kheiv/OneDrive/Documents/School/example_directory", "random text for assignment", "Not random text for assignment")
