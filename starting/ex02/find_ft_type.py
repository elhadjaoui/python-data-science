def all_thing_is_obj(object: any) -> int:

    class_name = object.__class__.__name__
    class_type = object.__class__
    if class_name == "str":
        print(f"{object} is in the kitchen :", class_type)
    elif object.__class__.__name__ == "int":
        print("Type not found")
    else:
        print(f"{class_name.title()} :", class_type)
    return 42
