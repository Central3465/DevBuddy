import uuid

def generate_uuid(option):
    if option.lower() == "random":
        return str(uuid.uuid4())
    elif option.lower() == "time":
        return str(uuid.uuid1())
    elif option.lower() == "name":
        namespace = uuid.NAMESPACE_DNS
        name = str(input("enter a name for uuid generation: "))
        return str(uuid.uuid5(namespace, name))
    else:
        raise ValueError("invalid option")