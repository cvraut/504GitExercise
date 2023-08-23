# this script contains two functions to count the frequency of characters in a string

from collections import Counter

def count_frequency(string: str) -> dict:
    """
    This function counts the frequency of each character in a string and returns a dictionary.

    Args:
        string (str): The string to count the frequency of characters.

    Returns:
        dict: A dictionary containing the frequency of each character in the string.
    """
    return Counter(string)


def print_frequency(frequency_dict: dict) -> None:
    """
    This function takes in a dictionary containing the frequency of each character and prints the frequency of each key.

    Args:
        frequency_dict (dict): A dictionary containing the frequency of each character.
    """
    print('Frequency of characters:')
    total = float(sum([cnt for cnt in frequency_dict.values()]))
    for char in frequency_dict.keys():
        print(char + ':' + str(frequency_dict[char]/total))

if __name__ == '__main__':
    print_frequency(count_frequency('ATCTGACGCGCGCCGC'))
