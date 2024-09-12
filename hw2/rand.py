import secrets

def random_array(arr):
    for i in range(len(arr)):
        arr[i] = secrets.randbelow(20) + 1
    return arr
