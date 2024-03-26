def NULL_not_found(object: any) -> int:
    class_name = object.__class__.__name__
    class_type = object.__class__
    if object.__class__.__name__ == "str":
        print("Type not found")
    elif object.__class__.__name__ == "float":
        print('Cheese:', class_type)
    else:
        print(f"{class_name} :", class_type)
    return 1