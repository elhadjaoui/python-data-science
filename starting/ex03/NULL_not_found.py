def NULL_not_found(object: any) -> int:
    class_name = object.__class__.__name__
    class_type = object.__class__
    if class_name == "NoneType":
        print(f"Nothing: {object} { class_type}")
    elif class_name == "int":
        print(f"Zero: {object} { class_type}")
    elif class_name == "bool":
        print(f"Fake: {object} { class_type}")
    elif class_name == "float":
        print(f"Cheese: {object} { class_type}")
    elif class_name == "str" and not object:
        print(f"Empty: {object} { class_type}")
    else:
        print("Type not Found")
        return 1
    return 0
