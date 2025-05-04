# General function to print the program header.
def print_feature_header(feature_name):
    title_text = f"--- Python Toolkit - {feature_name} ---"
    total_width = len(title_text)
    print("-" * total_width)
    print(title_text)
    print("-" * total_width)