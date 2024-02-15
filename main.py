"""
The code extracts data from file in lines.
Then it groups it in pyramid_dict dictionary.
Then I get all the numbers from dictionary.
Then I create a pyramid from it.
Then I extract important numbers from the pyramid.
Then I got through list of data from pyramid_dict using important numbers as Keys.
Then I return it.
"""

def decode(message_file):
    # Read the contents of the file
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Create a dictionary to store the key-value pairs
    pyramid_dict = {}

    # Extract numbers and words from each line and store them in the dictionary
    for line in lines:
        parts = line.strip().split()
        key = int(parts[0])
        value = parts[1]
        pyramid_dict[key] = value

    # Extract numbers from each line and arrange them into a pyramid
    pyramid_numbers = list(pyramid_dict.keys())

    # Sort the numbers to create the pyramid structure
    pyramid_numbers.sort()

    # Create pyramids
    pyramid = create_pyramid(pyramid_numbers)

    # Get important numbers from a pyramid
    important_numbers = get_last_numbers(pyramid)

    # Create a list to store the words corresponding to the decoded message
    decoded_words = [pyramid_dict[key] for key in important_numbers]

    # Join the decoded words to form the final message
    decoded_message = ' '.join(decoded_words)

    return decoded_message


def create_pyramid(pyramid_numbers):
    pyramid = []
    current_num = 1

    while pyramid_numbers:
        row = list(range(current_num, current_num + len(pyramid)))
        pyramid.append(row)
        current_num += len(row)
        pyramid_numbers = pyramid_numbers[len(row):]
    pyramid.pop(0)
    return pyramid


def get_last_numbers(pyramid):
    last_numbers = [row[-1] for row in pyramid]
    return last_numbers


# Main:
message_file = 'coding_qual_input.txt'
result = decode(message_file)
print(result)
