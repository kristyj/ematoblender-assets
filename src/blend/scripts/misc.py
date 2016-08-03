

def get_random_color():
    """Generate rgb using a list comprehension """
    import random
    r, g, b = [random.random() for i in range(3)]
    return r, g, b, 1