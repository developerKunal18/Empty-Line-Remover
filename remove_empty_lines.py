input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

try:
    with open(input_file, "r") as file:
        lines = file.readlines()

    with open(output_file, "w") as file:
        for line in lines:
            if line.strip():
                file.write(line)

    print("Empty lines removed successfully.")

except FileNotFoundError:
    print("File not found.")
