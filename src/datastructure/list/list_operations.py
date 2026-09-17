"""List Operations Module
This module contains functions to perform various operations on lists in Python.
Functions:
- add_element: Add an element to the list.
- remove_element: Remove an element from the list.
- find_element: Find an element in the list.
- sort_list: Sort the list in ascending order.
- reverse_list: Reverse the order of elements in the list.
"""

employes = ["Alice", "Bob", "Charlie", "David", "Eve"]


# Function to add an element to the list
def change_employee_name_case(employee_list) -> None:
    """Change the case of employee names in the list."""
    employee_list = list(map(str.upper, employee_list))
    return employee_list


if __name__ == "__main__":
    print("*" * 40)
    print("Welcome to the List Operations Project")
    print("*" * 40)
    print(f"Original Employee List: {employes}")
    updated_employes = change_employee_name_case(employes)
    print(f"Updated Employee List: {updated_employes}")
