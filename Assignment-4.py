
# Task 1

try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for line_number, line in enumerate(file, 1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 2

def write_and_append_to_file():
    """
    Takes user input, writes it to a file, appends data, and then reads and displays the final content.
    """
    filename = "output.txt"

    # 1. Take user input and write to the file
    try:
        user_input = input("Enter text to write to the file: ")
        with open(filename, "w") as file:
            file.write(user_input + "\n")  # Add a newline character for better readability
        print(f"Data successfully written to {filename}.")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

    # 2. Append additional data to the same file
    try:
        additional_data = input("Enter additional text to append: ")
        with open(filename, "a") as file:
            file.write(additional_data + "\n")  # Add a newline character
        print(f"Data successfully appended to {filename}.")
    except Exception as e:
        print(f"Error appending to file: {e}")
        return

    # 3. Read and display the final content of the file
    try:
        print(f"\nFinal content of {filename}:")
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())  # Remove leading/trailing whitespace and newline
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found (this should not happen).")
    except Exception as e:
        print(f"Error reading from file: {e}")

if __name__ == "__main__":
    write_and_append_to_file()

