# Task 1
def get_student_marks():
    """
    Creates a dictionary of student marks, asks for a student's name,
    retrieves and displays the marks, or shows a message if not found.
    """
    student_marks = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95,
        "Eve": 88
    }

    student_name = input("Enter the student's name: ")

    if student_name in student_marks:
        print(f"{student_name}'s marks: {student_marks[student_name]}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    get_student_marks()


#Task 2
def list_operations():
    """
    Creates a list of numbers, extracts the first five, reverses them, and prints both.
    """
    # 1. Creates a list of numbers from 1 to 10
    original_list = list(range(1, 11))
    print(f"Original list: {original_list}")

    # 2. Extracts the first five elements from the list
    extracted_list = original_list[:5]
    print(f"Extracted first five elements: {extracted_list}")

    # 3. Reverses these extracted elements
    reversed_list = extracted_list[::-1]
    print(f"Reversed extracted elements: {reversed_list}")

if __name__ == "__main__":
    list_operations()
