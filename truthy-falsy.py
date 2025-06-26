import ast

# uses ast.literal_eval() - converts a string to a Python literal
# uses bool() cast - converts a value to its truthiness
def tf_status(code_str):
    """Evaluate and print the truthiness of Python code string"""
    if not code_str.strip():
        print(f"Code: {code_str} -> False (empty string)")
        return
        
    try:
        result = ast.literal_eval(code_str)
        print(f"Code: {code_str} -> {bool(result)}")
    except (ValueError, SyntaxError):
        print(f"Code: {code_str} -> True (non-empty string)")

# Example usage
if __name__ == "__main__":
    tf_status("")  # Should print False
    tf_status("0")  # Should print False
    tf_status("1")  # Should print True
    tf_status("[]")  # Should print False
    tf_status("[1,2]")  # Should print True
    tf_status("'hello'")  # Should print True
    tf_status("None")  # Should print False
    tf_status("True")  # Should print True
    tf_status("False")  # Should print False
    tf_status("42")  # Should print True
    tf_status("{}")  # Should print True
