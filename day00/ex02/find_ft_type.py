def all_thing_is_obj(object: any) -> int:
    id = ""
    if isinstance(object, list):
        id = "List"
    elif isinstance(object, tuple):
        id = "Tuple"
    elif isinstance(object, set):
        id = "Set"
    elif isinstance(object, dict):
        id = "Dict"
    elif isinstance(object, str):
        id = f"{object} is in the kitchen"
    # check if type found 
    if not id:
        print("Type not found")
    else:
        print(f"{id} : {type(object)}")
    return 42
