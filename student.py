students = {}


def add_student(id, name):
    students[id] = name
    return True



def remove_student(id):
    if id in students:
        del students[id]
        return True
    return False


def search_student(id):
    if id in students:
        return students[id]
    else:
        return "Student Not Found"

def update_student(id, name):
    if id in students:
        students[id] = name
        return True
    return False