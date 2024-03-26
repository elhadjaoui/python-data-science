def all_thing_is_obj(object: any) -> int:
    uppercase_mapping = {
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D",
        "e": "E",
        "f": "F",
        "g": "G",
        "h": "H",
        "i": "I",
        "j": "J",
        "k": "K",
        "l": "L",
        "m": "M",
        "n": "N",
        "o": "O",
        "p": "P",
        "q": "Q",
        "r": "R",
        "s": "S",
        "t": "T",
        "u": "U",
        "v": "V",
        "w": "W",
        "x": "X",
        "y": "Y",
        "z": "Z",
    }
    class_name = object.__class__.__name__
    class_type = object.__class__
    if object.__class__.__name__ == "str":
        print(f"{object} is in the kitchen :", class_type)
    elif object.__class__.__name__ == "int":
        print("Type not found")
    else:
        uppercase_letter = uppercase_mapping.get(class_name[0])
        print(f"{uppercase_letter}{class_name[1:]} :", class_type)
        # print(f"{int(class_name[0]) - 32 + class_name[1:]} :", class_type)
    return 42
