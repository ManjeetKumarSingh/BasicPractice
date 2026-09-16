"""Data Structures in Python"""

from dictionaries.dict_operations import add_key_value, update_key_value

if __name__ == "__main__":
    print("*" * 40)
    print("Welcome to the Data Structures Project")
    print("*" * 40)
    print("Dictionary Operations:")
    my_dict = {"name": "Alice", "age": 25}
    print(f"Original Dictionary: {my_dict}")
    updated_dict = add_key_value(my_dict, "city", "Los Angeles")
    print(f"Updated Dictionary: {updated_dict}")
    print("=" * 40)
    my_dict1 = dict(name="Alice", age=25)
    print(f"Original Dictionary: {my_dict1}")
    print(f"TypedDict Operations :{my_dict1} ")
    updated_dict_using_typedDict = update_key_value(my_dict1, "city", "San Francisco")
    print(f"Updated Dictionary: {updated_dict_using_typedDict}")
