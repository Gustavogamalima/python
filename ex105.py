def studentGrades(*grades, sit=False):
    """
     -> Function to analyze notes and situations of several students.
     param grades: one or more student grades (multiple accepted)
     :param sit: optional value, indicating whether to add the situation
     :return: dictionary with various information about the class situation.
     """
    student = {'total': len(grades), 'bigger': max(grades), 'lowest': min(grades),
               'average': (sum(grades)) / len(grades)}
    if sit:
        if student['average'] >= 7:
            student['situation'] = 'Good'
        elif student['average'] >= 5:
            student['situation'] = 'Reasonable'
        else:
            student['situation'] = 'Bad'
    return student


answer = studentGrades(5.5, 0, 6.5, sit=True)
print(answer)
help(studentGrades)
