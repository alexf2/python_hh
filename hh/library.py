class Student:
    def __init__(self, name, interests):
        self.name = name
        self.interests = interests.split(',')

    def __repr__(self):
        return f'{self.name:<15}: {self.interests}'


class Library:
    def __init__(self, books):
        self.lib = {topic: book for book, topic in (
            book.split(':') for book in books.split(';'))}

    def __repr__(self):
        return f'{self.lib}'

    def compile_list(self, student: Student):
        books = [
            v for v in (
                self.lib.get(
                    topic,
                    None) for topic in student.interests)]

        books = list(filter(lambda item: item is not None, books))

        return f'{
            student.name}:{",".join(books) if len(books) else "Список пуст"}'


data = ((
    'Анна:Научная фантастика,Математика;Иван:История,Документальная литература',
    'Преступление и наказание:Художественная литература;Задача трёх тел:Научная фантастика;История государства российского:История'),
    ('София:История;Дмитрий:Математика,Физика;Екатерина:Химия',
     'Квантовая механика:Физика;Занимательная геохимия:Химия;Методы теории функции комплексного переменного:Математика'),
    ('София:История;Дмитрий:Математика', 'Квантовая механика:Физика'))

res = []
for s, books in data:
    students = [Student(name, interests) for name, interests in
                (student.split(':') for student in s.split(';'))]

    library = Library(books)

    tmp = []
    for s in students:
        tmp.append(library.compile_list(s))

    res.append(tmp)


for r in res:
    print(';'.join(r))
