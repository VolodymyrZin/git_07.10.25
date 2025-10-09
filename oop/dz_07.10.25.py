# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть
# об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент", який
# дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть його
# середній бал.

class Student:

    def __init__(self, name, surname, age, average_score):
        """
        Constructor
        :param name:
        :param surname:
        :param age:
        :param average_score:
        """
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def change_average_score(self, new_score):
        """
        Changes the average score of the student
        :param new_score:
        :return:
        """
        self.average_score = new_score
        return new_score

top_student = Student(name='Vano', surname='Dubidze', age=25, average_score=50)
print(f"Ім'я студента: {top_student.name}, прізвище: {top_student.surname}, "
      f"вік: {top_student.age}, середній бал: {top_student.average_score}")

print("До зміни середнього балу:", top_student.average_score)

top_student.change_average_score(80)

print("Після зміни середнього балу:", top_student.average_score)
