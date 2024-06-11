
def NULL_not_found(object: any) -> int:
    name = ""

    if isinstance(object, float) and object != object:
        name = "Cheese"
    elif type(object) is bool and object is False:
        name = "False"
    elif isinstance(object, int) and object == 0:
        name = "Zero"
    elif isinstance(object, str) and not object:
        name = "Empty"
    elif object is None:
        name = "Nothing"
    
    if not name:
        print("Type not found")
        return 1
    else:
        print(f"{name}: {object} {type(object)}")
        return 0