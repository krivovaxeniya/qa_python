import pytest
from main import BooksCollector


@pytest.fixture(scope="function")
def append_one_book_in_books_genre():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    return collector


@pytest.fixture(scope="function")
def append_five_book_and_genre_in_books_genre():
    collector = BooksCollector()
    book_genre_list = [['Гордость и предубеждение и зомби', 'Ужасы'], ['12 стульев', 'Комедии'],
                       ['Золотой теленок', 'Комедии'], ['Зов Ктулху', 'Ужасы'], ['Трое в лодке', 'Комедии']]
    for el in book_genre_list:
        collector.add_new_book(el[0])
        collector.set_book_genre(el[0], el[1])
    return collector

@pytest.fixture(scope="function")
def append_five_book_with_other_genre():
    collector = BooksCollector()
    book_genre_list = [['Гордость и предубеждение и зомби', 'Детективы'], ['12 стульев', 'Комедии'],
                       ['Незнайка', 'Мультфильмы'], ['Зов Ктулху', 'Ужасы'], ['Алиса в стране чудес', 'Фантастика']]
    for el in book_genre_list:
        collector.add_new_book(el[0])
        collector.set_book_genre(el[0], el[1])
    return collector

@pytest.fixture(scope="function")
def append_three_books_in_favorite():
    collector = BooksCollector()
    book_genre_list = [['Гордость и предубеждение и зомби', 'Детективы'], ['12 стульев', 'Комедии'],
                       ['Незнайка', 'Мультфильмы'], ['Зов Ктулху', 'Ужасы'], ['Алиса в стране чудес', 'Фантастика']]
    for el in book_genre_list:
        collector.add_new_book(el[0])
        collector.set_book_genre(el[0], el[1])
    collector.add_book_in_favorites('12 стульев')
    collector.add_book_in_favorites('Зов Ктулху')
    collector.add_book_in_favorites('Алиса в стране чудес')
    return collector