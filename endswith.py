def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a.endswith(b):
        return True
    if b.endswith(a):
        return True
    else:
        return False



print(end_other('Z', '12xz'))
