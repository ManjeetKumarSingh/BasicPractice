"""Set Operations Module
This module contains functions to perform various operations on sets in Python.
Functions:
- add_element: Add an element to the set.
- remove_element: Remove an element from the set.
- find_element: Find an element in the set.
- union_sets: Perform union operation on two sets.
- intersection_sets: Perform intersection operation on two sets.
"""

emloyees_set = {"Alice", "Bob", "Charlie", "David", "Eve"}
print(f"Original Employee Set: {type(emloyees_set)}, {emloyees_set}")


# Function for removing the name using the filter function and lambda function
def remove_employee_from_list(employee_set, name) -> None:
    """Change the case of employee names in the set."""
    emloyee_set = set(filter(lambda x: x.lower() != name.lower(), employee_set))
    return emloyee_set


removed_employee_set = remove_employee_from_list(emloyees_set, "Bob")
print(f"Updated Employee Set: {type(removed_employee_set)}, {removed_employee_set}")
