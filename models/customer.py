class Customer():
    """[summary]
    """
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
