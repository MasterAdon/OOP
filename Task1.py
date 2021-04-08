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
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.grades_average} " \
               f" \nКурсы в процесе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]} \nЗавершенные курсы: {self.finished_courses[0]} "

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

some_lecturer = Lecturer('Ivan', 'Ivanov')
some_lecturer.courses_attached += ['Python']

any_student = Student('Petr', 'Petrov', 'man')
any_student.courses_in_progress += ['Python']

any_student.rate_lec(some_lecturer, 'Python', 10)
any_student.rate_lec(some_lecturer, 'Python', 7)

# print(some_lecturer.grades)
# Реализована возможность получения оценки для преподователей, по аналогии с оценками студентов

for a, b in some_lecturer.grades.items():
    some_lecturer.grade_average = sum(b) / len(b)
# Расчет средней оценки лектора
for c, d in best_student.grades.items():
    best_student.grades_average = sum(d) / len(d)
# Расчет средней оценки студента
some_lecturer1 = Reviewer('Some', 'Buddy')

# print(some_lecturer1) #Вывод для проверяющих
# print(some_lecturer) #Вывод для лекторов
# print(best_student)  #Вывод для студентов


# Выполняем 4-ю задачу из ДЗ.

reviewer1 = Reviewer('Oleg', 'Olegov')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['GIT']
reviewer2 = Reviewer('Anton', 'Antonov')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['GIT']

lecturer1 = Lecturer('Vasya', 'Vasin')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['GIT']

lecturer2 = Lecturer('Efim', 'Efimov')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['GIT']

student1 = Student('Denis', 'Denisov', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['GIT']
student1.finished_courses += ['Введение в програмирование']
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'GIT', 6)
reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'GIT', 7)


student2 = Student('Anya', 'Anina', 'female')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['GIT']
student2.finished_courses += ['Введение в програмирование']
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'GIT', 8)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'GIT', 9)

for course, grade in student1.grades.items():
    grades_average = sum(grade) / len(grade)
    a = {course: grades_average}
    student1.grades_average.update(a)

for course, grade in student2.grades.items():
    grades_average = sum(grade) / len(grade)
    a = {course: grades_average}
    student2.grades_average.update(a)

student1.rate_lec(lecturer1, 'Python', 9)
student1.rate_lec(lecturer1, 'GIT', 8)
student2.rate_lec(lecturer1, 'Python', 8)
student2.rate_lec(lecturer1, 'GIT', 7)
student1.rate_lec(lecturer2, 'Python', 10)
student1.rate_lec(lecturer2, 'GIT', 9)
student2.rate_lec(lecturer2, 'Python', 8)
student2.rate_lec(lecturer2, 'GIT', 10)

students_list = [student1, student2]  # Список обьектов учащихся

all_avg_grade_course = {}  # Перерасчет среднией оценки для всего курса

course_aver_item = {}  # Собираем словарь из средних оценок за курс

for personal in students_list:
    # print(personal.grades_average)
    for cour, gra in personal.grades_average.items():
        b = {cour: gra}
        course_aver_item.setdefault(cour, []).append(gra)

for course, grade in course_aver_item.items():
    course_avg_grade = sum(grade) / len(grade)
    m = {course: course_avg_grade}
    all_avg_grade_course.update(m)


# print(all_avg_grade_course)

def cur_avg_grad(students_list, course):  # Средняя оценка студентов за курс
    if course in all_avg_grade_course:
        print(f'Средняя оценка за домашниее задание на курсе {course} составляет {all_avg_grade_course[course]}')
    else:
        return print('За данный курс оценки не выставлялись')

# cur_avg_grad(students_list, 'GIT') # функция реализована

for course, grade in lecturer1.grades.items():
    grades_average = sum(grade) / len(grade)
    a = {course: grades_average}
    lecturer1.grade_average.update(a)

for course, grade in lecturer2.grades.items():
    grades_average = sum(grade) / len(grade)
    a = {course: grades_average}
    lecturer2.grade_average.update(a)





lecturer_list = [lecturer1, lecturer2]  # Список обьектов преподавателей

all_avg_grad_lec = {} # Перерасчет средней оценки

course_aver_lec = {} # Словарь из средних оценок

for personal in lecturer_list:
    # print(personal.grade_average)
    for cou, gr in personal.grade_average.items():
        c = {cou: gr}
        course_aver_lec.setdefault(cou, []).append(gr)

for course, grade in course_aver_lec.items():
    course_avg_grade = sum(grade)/len(grade)
    t = {course: course_avg_grade}
    all_avg_grad_lec.update(t)

def avg_gra_lec(lecturer_list, course): # Средняя оценка за лекции
    if course in all_avg_grad_lec:
        print(f'Средняя оценка за лекции на курсе {course} составляет {all_avg_grad_lec[course]}')
    else:
        return print('Оценки за лекции не выставлялись')


# avg_gra_lec(lecturer_list, 'Python') # Функция реализована


