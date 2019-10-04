# Implement your is_all_strings function below:
def is_all_strings(strings):
    return all(type(item) == str for item in strings)