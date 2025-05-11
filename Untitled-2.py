class Book:
    def __init__(self, udk, author, title, year, count):
        self.udk = udk
        self.author = author
        self.title = title
        self.year = year
        self.count = count

    def __str__(self):
        return f"УДК: {self.udk}, Автор: {self.author}, Название: {self.title}, Год: {self.year}, В наличии: {self.count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена.")

    def find_book_by_udk(self, udk):
        for book in self.books:
            if book.udk == udk:
                return book
        return None

    def issue_book(self, udk):
        book = self.find_book_by_udk(udk)
        if not book:
            print("Книги нет в наличии.")
            return False
        if book.count <= 0:
            print("Книга находится на руках.")
            return False
        book.count -= 1
        print(f"Выдана книга '{book.title}'. Осталось: {book.count}")
        return True

    def return_book(self, udk):
        book = self.find_book_by_udk(udk)
        if not book:
            print("Книга не найдена.")
            return False
        book.count += 1
        print(f"Возвращена книга '{book.title}'. Теперь в наличии: {book.count}")
        return True

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            print("\nСписок всех книг в библиотеке:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")


def main():
    library = Library()

    # Предзагрузка книг
    print("Добавляем предзагруженные книги...")
    books_data = [
        ("23.02", "Толстой Л.Н.", "Война и мир", 1869, 5),
        ("84.1", "Достоевский Ф.М.", "Преступление и наказание", 1866, 3),
        ("11.88", "Некрасов Н.А.", "Кому на Руси жить хорошо", 1879, 3),
        ("11.2", "Чехов А.П.", "Три сестры", 1901, 4),
        ("18.7", "Гоголь Н.В.", "Мертвые души", 1842, 2),
        ("5.01", "Пушкин А.С.", "Евгений Онегин", 1833, 6),
        ("56.34", "Шолохов М.А.", "Тихий Дон", 1940, 4),
        ("91.3", "Горький М.", "На дне", 1902, 2),
        ("34.4", "Шолохов М.", "Судьба человека", 1958, 4),
        ("45.9", "Лермонтов М.Ю.", "Герой нашего времени", 1840, 0),
        ("67.1", "Грибоедов А.С.", "Горе от ума", 1825, 1)
    ]

    for udk, author, title, year, count in books_data:
        library.add_book(Book(udk, author, title, year, count))
    print("Предзагрузка книг завершена.\n")

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Выдать книгу")
        print("3. Вернуть книгу")
        print("4. Показать все книги")
        print("5. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                udk = input("Введите УДК: ")
                author = input("Автор: ")
                title = input("Название: ")
                year = int(input("Год издания: "))
                count = int(input("Количество экземпляров: "))
                library.add_book(Book(udk, author, title, year, count))

            elif choice == "2":
                udk = input("Введите УДК книги для выдачи: ")
                library.issue_book(udk)

            elif choice == "3":
                udk = input("Введите УДК книги для возврата: ")
                library.return_book(udk)

            elif choice == "4":
                library.display_books()

            elif choice == "5":
                print("Выход...")
                break

            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректные данные.")


if __name__ == "__main__":
    main()