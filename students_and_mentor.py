class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached :
            if course in lector.grades_lecturer:
                lector.grades_lecturer[course] += [grade]
            else:
                lector.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        list_grades=[]
        for i in self.grades.values():
            for j in i:
                list_grades.append(j)

        average_grades = round(sum(list_grades)/len(list_grades),2)
        return average_grades

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not o Student')
            return
        return self.average_grades() < other.average_grades()

    def __str__(self):
        str_courses_in_progress = ', '.join(self.courses_in_progress)
        str_finished_courses = ', '.join(self.finished_courses)

        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grades()}\n' \
              f'Курсы в процессе изучения: {str_courses_in_progress}\n' \
              f'Завершенные курсы: {str_finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


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
        res = f'Имя:{self.name}\nФамилия:{self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

    def average_grades_lecturer(self):
        list_grades_lecturer = []
        for i in self.grades_lecturer.values():
            for j in i:
                list_grades_lecturer.append(j)
        average_grades_lecturer = round(sum(list_grades_lecturer) / len(list_grades_lecturer), 2)
        return average_grades_lecturer

    def __str__(self):
        res = f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.average_grades_lecturer()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Not o Mentor')
            return
        return self.average_grades_lecturer() < other.average_grades_lecturer()

def average_grades_student_in_course(course, student_list):
    student_in_course = []
    all_rates_in_course = []
    for student in student_list:
        if course in student.courses_in_progress + student.finished_courses:
            student_in_course.append(student)
            all_rates_in_course += student.grades[course]
    if student_in_course == []:
        print(f'Студенты {student_list} не проходили курс {course}')
    elif len(all_rates_in_course) != 0:
        res = sum(all_rates_in_course) / len(all_rates_in_course)
    else:
        res = 0
    result = print(f'Средняя оценка студентов за курс {course}: {res}')
    return result

def average_grades_lector_in_course(course, lector_list):
    lector_in_course = []
    all_rates_in_course = []
    for lector in lector_list:
        if course in lector.courses_attached:
            lector_in_course.append(lector)
            all_rates_in_course += lector.grades_lecturer[course]
    if lector_in_course == []:
        print(f'Лекторы {lector_list} не проводили курс {course}')
    elif len(all_rates_in_course) != 0:
        res = sum(all_rates_in_course) / len(all_rates_in_course)
    else:
        res = 0
    result = print(f'Средняя оценка лекторов за курс {course}: {res}')
    return result





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
best_student.finished_courses += ['Введение в программирование PRO']

best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']
best_student_1.courses_in_progress += ['Git']
best_student_1.finished_courses += ['Введение в программирование']
best_student_1.finished_courses += ['Введение в программирование PRO']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Nik', 'Kin')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer_1 = Reviewer('Nik', 'Kin')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Git']

cool_lecturer = Lecturer('Nik1', 'Kin1')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

cool_lecturer_1 = Lecturer('Nik2', 'Kin2')
cool_lecturer_1.courses_attached += ['Python']
cool_lecturer_1.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Git', 7)
cool_reviewer.rate_hw(best_student, 'Git', 8)

cool_reviewer.rate_hw(best_student_1, 'Python', 10)
cool_reviewer.rate_hw(best_student_1, 'Python', 10)
cool_reviewer.rate_hw(best_student_1, 'Python', 10)
cool_reviewer.rate_hw(best_student_1, 'Git', 10)
cool_reviewer.rate_hw(best_student_1, 'Git', 10)
cool_reviewer.rate_hw(best_student_1, 'Git', 10)

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 7)
best_student.rate_lecturer(cool_lecturer, 'Git', 8)
best_student.rate_lecturer(cool_lecturer, 'Git', 9)
best_student.rate_lecturer(cool_lecturer, 'Git', 8)

best_student.rate_lecturer(cool_lecturer_1, 'Python', 10)
best_student.rate_lecturer(cool_lecturer_1, 'Python', 8)
best_student.rate_lecturer(cool_lecturer_1, 'Python', 10)
best_student.rate_lecturer(cool_lecturer_1, 'Git', 10)
best_student.rate_lecturer(cool_lecturer_1, 'Git', 10)
best_student.rate_lecturer(cool_lecturer_1, 'Git', 10)


#print(best_student)
#print(best_student < best_student_1)
# print(cool_reviewer)
#print(cool_lecturer)
#print(cool_lecturer < cool_lecturer_1)
# print(best_student.grades)
# print(best_student.grades_lecturer)

#average_grades_student_in_course('Python', [best_student, best_student_1])
#average_grades_lector_in_course('Python', [cool_lecturer, cool_lecturer_1])