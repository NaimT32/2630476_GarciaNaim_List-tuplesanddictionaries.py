# LIST, TUPLES AND DICTIONARIES

# Student name: Naim Tadeo Garcia Briones
# Student(matricula): 2630476
# Group: 1-1
# Submission date: 18/10/2026
# Assignment: Python Lists, Tuples, and Dictionaries


# LIST, TUPLES AND DICTIONARIES

# A list is an ordered and mutable collection, so items can be added or removed.
# A tuple is ordered but immutable, which makes it useful for fixed data such as
# coordinates. A dictionary stores key-value pairs, allowing information to be
# found through a descriptive key. This program uses collections in practical
# contexts including shopping lists, points, catalogs, grade records, word
# frequencies, and contacts. Each problem documents its inputs, outputs,
# validations, and test cases before using the selected data structure.


# PRINCIPLES AND BEST PRACTICES

# - Use lists when items need to be added or removed frequently.
# - Use tuples for fixed data, such as coordinates, that should not change.
# - Use dictionaries to find values by a meaningful key, such as a product name.
# - Do not change a list inside a for loop unless the behavior is intentional.
# - Use descriptive dictionary keys such as name, price, and phone.
# - Keep identifiers and messages clear so users understand the program result.


import math


PASSING_GRADE = 70.0
SIMPLE_PUNCTUATION = (".", ",", ";", ":", "!", "?")
PRODUCT_PRICES = {
    "apple": 10.0,
    "banana": 5.5,
    "orange": 8.0,
}
STUDENT_GRADES = {
    "alice": [90.0, 85.0, 95.0],
    "bob": [65.0, 60.0, 70.0],
    "carol": [70.0],
}


def format_boolean(value):
    """Return a boolean as lowercase English text for the required output."""
    return str(value).lower()


def normalize_text(text):
    """Remove leading, trailing, and repeated internal whitespace."""
    return " ".join(text.strip().split())


def parse_finite_float(value_text):
    """Convert text to a finite float, or return None when conversion fails."""
    try:
        value = float(value_text)
    except (TypeError, ValueError):
        return None

    if not math.isfinite(value):
        return None
    return value


def parse_positive_integer(value_text):
    """Convert text to an integer greater than zero, or return None."""
    try:
        value = int(value_text)
    except (TypeError, ValueError):
        return None

    if value <= 0:
        return None
    return value



# Problem 1: Shopping list basics (list operations)
# Description:
#   This problem creates a list from comma-separated products, adds one product
#   at the end, counts the items, and searches for another product. Products are
#   normalized to lowercase so searches are case-insensitive.
# Inputs:
#   - initial_items_text: comma-separated product names.
#   - new_item and search_item: non-empty product names.
# Outputs:
#   - Items list, Total items, and Found item: true or false.
# Validations:
#   - The initial text, new item, and search item cannot be empty.
#   - Empty pieces created by extra commas are ignored after stripping spaces.
# Test cases:
#   1) Normal: "apple, banana, orange", "milk", "banana" -> found true
#   2) Border: "apple", "apple", "apple" -> two items, found true
#   3) Error: "   ", "milk", "milk" -> Error: invalid input

def process_shopping_list(initial_items_text, new_item, search_item):
    """Return a shopping list result dictionary, or None when input is invalid."""
    if initial_items_text.strip() == "":
        return None

    items_list = []
    for raw_item in initial_items_text.split(","):
        cleaned_item = normalize_text(raw_item).lower()
        if cleaned_item != "":
            items_list.append(cleaned_item)

    normalized_new_item = normalize_text(new_item).lower()
    normalized_search_item = normalize_text(search_item).lower()
    if not items_list or normalized_new_item == "" or normalized_search_item == "":
        return None

    items_list.append(normalized_new_item)
    is_in_list = normalized_search_item in items_list
    return {
        "items_list": items_list,
        "total_items": len(items_list),
        "is_in_list": is_in_list,
    }



# Problem 2: Points and distances with tuples
# Description:
#   This problem creates two immutable coordinate tuples, calculates their
#   Euclidean distance, and creates a new tuple for the midpoint.
# Inputs:
#   - x1, y1, x2, y2: finite float coordinates.
# Outputs:
#   - Point A, Point B, Distance, and Midpoint.
# Validations:
#   - Each coordinate must be convertible to a finite float.
# Test cases:
#   1) Normal: (0, 0), (3, 4) -> distance 5.00, midpoint (1.50, 2.00)
#   2) Border: (1, 1), (1, 1) -> distance 0.00, midpoint (1.00, 1.00)
#   3) Error: (a, 0), (3, 4) -> Error: invalid input

def calculate_point_data(x1_text, y1_text, x2_text, y2_text):
    """Return point tuples, distance, and midpoint, or None when invalid."""
    x1 = parse_finite_float(x1_text)
    y1 = parse_finite_float(y1_text)
    x2 = parse_finite_float(x2_text)
    y2 = parse_finite_float(y2_text)

    if x1 is None or y1 is None or x2 is None or y2 is None:
        return None

    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    return point_a, point_b, distance, midpoint



# Description:
#   This problem uses a dictionary that associates product names with unit
#   prices. It calculates an order total only when the requested product exists.
# Inputs:
#   - product_name: a non-empty product name.
#   - quantity: an integer greater than zero.
# Outputs:
#   - Unit price, Quantity, and Total; or an error when the product is missing.
# Validations:
#   - The product name cannot be empty and quantity must be a positive integer.
#   - The product key must exist in the product_prices dictionary.
# Test cases:
#   1) Normal: "apple", 3 -> unit price 10.00, total 30.00
#   2) Border: "banana", 1 -> unit price 5.50, total 5.50
#   3) Error: "pear", 2 -> Error: product not found

def calculate_product_order(product_name, quantity_text):
    """Return an order result status and data for the catalog lookup."""
    normalized_product_name = normalize_text(product_name).lower()
    quantity = parse_positive_integer(quantity_text)

    if normalized_product_name == "" or quantity is None:
        return "invalid", None

    unit_price = PRODUCT_PRICES.get(normalized_product_name)
    if unit_price is None:
        return "not_found", None

    total_price = unit_price * quantity
    return "ok", (unit_price, quantity, total_price)



# Problem 4: Student grades with dict and list
# Description:
#   This problem uses a dictionary where each student key points to a list of
#   grades. It calculates the average and a boolean that states if the student
#   passed with an average of at least 70.0.
# Inputs:
#   - student_name: a non-empty student name.
# Outputs:
#   - Grades, Average, and Passed: true or false; or a not-found error.
# Validations:
#   - The name must not be empty, must exist as a dictionary key, and its grade
#     list must not be empty before calculating the average.
# Test cases:
#   1) Normal: "Alice" -> average 90.00, passed true
#   2) Border: "Carol" -> average 70.00, passed true
#   3) Error: "David" -> Error: student not found

def get_student_report(student_name):
    """Return a student report status and data from the grades dictionary."""
    normalized_student_name = normalize_text(student_name).lower()
    if normalized_student_name == "":
        return "invalid", None

    grades_list = STUDENT_GRADES.get(normalized_student_name)
    if grades_list is None:
        return "not_found", None
    if len(grades_list) == 0:
        return "empty_grades", None

    average = sum(grades_list) / len(grades_list)
    is_passed = average >= PASSING_GRADE
    return "ok", (grades_list, average, is_passed)


# Problem 5: Word frequency counter (list + dict)
# Description:
#   This problem changes a sentence to lowercase, removes simple punctuation,
#   creates a list of words, and counts each word in a frequency dictionary.
#   The first word with the maximum count is selected if there is a tie.
# Inputs:
#   - sentence: a non-empty text string.
# Outputs:
#   - Words list, Frequencies, and Most common word.
# Validations:
#   - The sentence cannot be empty after stripping or after punctuation removal.
# Test cases:
#   1) Normal: "red blue red" -> {"red": 2, "blue": 1}, most common red
#   2) Border: "word" -> {"word": 1}, most common word
#   3) Error: "!!!" -> Error: invalid input

def count_word_frequencies(sentence):
    """Return word list and frequency data, or None when the sentence is invalid."""
    normalized_sentence = sentence.strip().lower()
    if normalized_sentence == "":
        return None

    for punctuation_mark in SIMPLE_PUNCTUATION:
        normalized_sentence = normalized_sentence.replace(punctuation_mark, "")

    words_list = normalized_sentence.split()
    if not words_list:
        return None

    frequency_dict = {}
    for word in words_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    most_common_word = words_list[0]
    for word in frequency_dict:
        if frequency_dict[word] > frequency_dict[most_common_word]:
            most_common_word = word

    return words_list, frequency_dict, most_common_word



# Problem 6: Simple contact book (dictionary CRUD)
# Description:
#   This problem uses a contact dictionary. ADD saves or updates a contact,
#   SEARCH looks up a phone number, and DELETE removes an existing contact.
# Inputs:
#   - action_text: ADD, SEARCH, or DELETE.
#   - name: a non-empty contact name; phone is also required for ADD.
# Outputs:
#   - A saved, found, deleted, invalid-action, or not-found result message.
# Validations:
#   - The action is normalized to uppercase and must be valid.
#   - The name cannot be empty; ADD also requires a non-empty phone value.
# Test cases:
#   1) Normal: SEARCH, "Alice" -> Phone: 555-0101
#   2) Border: ADD, "Dora", "555-0104" -> contact saved (new key)
#   3) Error: UPDATE, "Alice" -> Error: invalid input

def create_initial_contacts():
    """Create and return a new initial contact dictionary."""
    return {
        "alice": "555-0101",
        "bob": "555-0102",
        "carol": "555-0103",
    }


def manage_contact(contacts, action_text, name_text, phone_text=""):
    """Perform one contact action and return a status plus its result data."""
    action = action_text.strip().upper()
    if action not in ("ADD", "SEARCH", "DELETE"):
        return "invalid_action", None

    normalized_name = normalize_text(name_text)
    contact_key = normalized_name.lower()
    if contact_key == "":
        return "invalid", None

    if action == "ADD":
        normalized_phone = normalize_text(phone_text)
        if normalized_phone == "":
            return "invalid", None
        contacts[contact_key] = normalized_phone
        return "saved", (normalized_name, normalized_phone)

    if action == "SEARCH":
        phone = contacts.get(contact_key)
        if phone is None:
            return "not_found", None
        return "found", phone

    if contact_key not in contacts:
        return "not_found", None

    contacts.pop(contact_key)
    return "deleted", normalized_name


def print_problem_1():
    """Read and display the result for Problem 1."""
    print("\nProblem 1: Shopping list basics")
    initial_items_text = input("Enter comma-separated items: ")
    new_item = input("Enter new item: ")
    search_item = input("Enter item to search: ")
    result = process_shopping_list(initial_items_text, new_item, search_item)

    if result is None:
        print("Error: invalid input")
        return

    print(f"Items list: {result['items_list']}")
    print(f"Total items: {result['total_items']}")
    print(f"Found item: {format_boolean(result['is_in_list'])}")


def print_problem_2():
    """Read and display the result for Problem 2."""
    print("\nProblem 2: Points and distances with tuples")
    x1_text = input("Enter x1: ")
    y1_text = input("Enter y1: ")
    x2_text = input("Enter x2: ")
    y2_text = input("Enter y2: ")
    result = calculate_point_data(x1_text, y1_text, x2_text, y2_text)

    if result is None:
        print("Error: invalid input")
        return

    point_a, point_b, distance, midpoint = result
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance:.2f}")
    print(f"Midpoint: ({midpoint[0]:.2f}, {midpoint[1]:.2f})")


def print_problem_3():
    """Read and display the result for Problem 3."""
    print("\nProblem 3: Product catalog with dictionary")
    product_name = input("Enter product name: ")
    quantity_text = input("Enter quantity: ")
    status, data = calculate_product_order(product_name, quantity_text)

    if status == "invalid":
        print("Error: invalid input")
        return
    if status == "not_found":
        print("Error: product not found")
        return

    unit_price, quantity, total_price = data
    print(f"Unit price: {unit_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: {total_price:.2f}")


def print_problem_4():
    """Read and display the result for Problem 4."""
    print("\nProblem 4: Student grades with dict and list")
    student_name = input("Enter student name: ")
    status, data = get_student_report(student_name)

    if status == "invalid":
        print("Error: invalid input")
        return
    if status == "not_found":
        print("Error: student not found")
        return
    if status == "empty_grades":
        print("Error: grades list is empty")
        return

    grades_list, average, is_passed = data
    print(f"Grades: {grades_list}")
    print(f"Average: {average:.2f}")
    print(f"Passed: {format_boolean(is_passed)}")


def print_problem_5():
    """Read and display the result for Problem 5."""
    print("\nProblem 5: Word frequency counter")
    sentence = input("Enter sentence: ")
    result = count_word_frequencies(sentence)

    if result is None:
        print("Error: invalid input")
        return

    words_list, frequency_dict, most_common_word = result
    print(f"Words list: {words_list}")
    print(f"Frequencies: {frequency_dict}")
    print(f"Most common word: {most_common_word}")


def print_problem_6(contacts):
    """Read and display the result for Problem 6."""
    print("\nProblem 6: Simple contact book")
    action_text = input("Enter action (ADD/SEARCH/DELETE): ")
    name_text = input("Enter contact name: ")
    phone_text = ""
    if action_text.strip().upper() == "ADD":
        phone_text = input("Enter phone: ")

    status, data = manage_contact(contacts, action_text, name_text, phone_text)
    if status == "invalid_action" or status == "invalid":
        print("Error: invalid input")
    elif status == "saved":
        saved_name, saved_phone = data
        print(f"Contact saved: {saved_name}, {saved_phone}")
    elif status == "found":
        print(f"Phone: {data}")
    elif status == "deleted":
        print(f"Contact deleted: {data}")
    else:
        print("Error: contact not found")


def main():
    """Run the six required collection problems in order."""
    print("Python Lists, Tuples, and Dictionaries Assignment")
    print_problem_1()
    print_problem_2()
    print_problem_3()
    print_problem_4()
    print_problem_5()
    contacts = create_initial_contacts()
    print_problem_6(contacts)


if __name__ == "__main__":
    main()



# CONCLUSIONS

# Lists are useful when a collection must change by adding or removing items.
# Tuples are suitable for fixed records, such as the coordinate pairs in this
# assignment. Dictionaries make lookup by a key fast and clear for catalogs and
# contacts. Combining dictionaries and lists is useful for records with several
# values, such as a student and their grades. Validating keys and empty lists
# prevents lookup errors and invalid calculations in these common patterns.



# REFERENCES

# 1) Python Software Foundation. "Sequence Types - list, tuple, range."
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 2) Python Software Foundation. "Mapping Types - dict."
#    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# 3) Python Software Foundation. "Data Structures." Python Tutorial.
#    https://docs.python.org/3/tutorial/datastructures.html
# 4) Python Software Foundation. "More Control Flow Tools." Python Tutorial.
#    https://docs.python.org/3/tutorial/controlflow.html
# 5) Python Software Foundation. "Built-in Functions." Python Documentation.
#    https://docs.python.org/3/library/functions.html
# 6) van Rossum, G., Warsaw, B., and Coghlan, A. "PEP 8 - Style Guide for
#    Python Code." https://peps.python.org/pep-0008/
# 7) OWASP Foundation. "Input Validation Cheat Sheet."
#    https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

