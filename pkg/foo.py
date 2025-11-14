PI = 3.14159

def calc(grade):
    if grade >= 90:
        return 'S'
    elif grade >= 80: 
        return 'A'
    elif grade >= 70: 
        return 'B'
    elif grade >= 60: 
        return 'C'
    else:
        return 'D'