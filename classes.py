class Leaf:
    """
    Word following n previous words
    """
    def __init__(self, name):
        if type(name) is str:
            self.name = name
        else:
            raise ValueError("Usage: name must be type string")


class Node:
    def __init__(self, ):
