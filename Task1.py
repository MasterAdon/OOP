class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_average = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress or self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.grades_average} ' \
               f' \nКурсы в процесе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]} \nЗавершенные курсы: {self.finished_courses[0]} '

    def __lt__(self, other):
        return self.grades_average < other.grades_average

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.grade_average = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grade_average} '

    def __gt__(self, other):
        return self.grade_average > other.grades_average

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в програмирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)


some_lecturer = Lecturer('Ivan', 'Ivanov')
some_lecturer.courses_attached += ['Python']

any_student = Student('Petr', 'Petrov', 'man')
any_student.courses_in_progress += ['Python']

any_student.rate_lec(some_lecturer, 'Python', 10)
any_student.rate_lec(some_lecturer, 'Python', 8)

# print(some_lecturer.grades)
# Реализована возможность получения оценки для преподователей, по аналогии с оценками студентов

for a, b in some_lecturer.grades.items():
    some_lecturer.grade_average = sum(b) // len(b)

# Расчет средней оценки лектора
for c, d in best_student.grades.items():
    best_student.grades_average = sum(d) // len(d)

# Расчет средней оценки стцдента
some_lecturer1 = Reviewer('Petr', 'Petrov')

# print(some_lecturer1) #Вывод для проверяющих
# print(some_lecturer) #Вывод для лекторов
# print(best_student)  #Вывод для студентов


