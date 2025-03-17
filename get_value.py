def get_value(obj, key):
    keys = key.split("/")
    for k in keys:
        if isinstance(obj, dict) and k in obj:
            obj = obj[k]
        else:
            return None
    return obj

obj1 = {"a":{"b":{"c":"d"}}}
obj2 = {"x":{"y":{"z":"a"}}}

def run_get_value():
    print(get_value(obj1, "a/b/c"))
    print(get_value(obj2, "x/y/z"))
    print(get_value(obj1, "a/b"))
    print(get_value(obj1, "a/y"))

def tests_get_value():
    assert get_value(obj1, "a/b/c") == "d"
    assert get_value(obj2, "x/y/z") == "a"
    assert get_value(obj1, "a/b") == {"c":"d"}
    assert get_value(obj1, "a/y") == None

run_get_value()
tests_get_value()