import random

def generateKeystream(size: int, seed: int):
    random.seed(seed)
    key = []
    
    for i in range(size):
        key.append(random.randint(0, 255))
    
    return key
