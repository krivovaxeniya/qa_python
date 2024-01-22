import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_books_genre_of_books_collector_true(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_favorites_of_books_collector_true(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_genre_of_books_collector_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_of_books_collector_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_two_books_shows_len_of_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_books_in_books_genre_shows_elements_of_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre() and 'Что делать, если ваш кот хочет вас убить' in collector.get_books_genre()

    def test_add_new_book_add_one_book_shows_genre_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_add_new_book_add_one_book_twice_shows_len_of_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name', ['', 'Гордость и предубеждение и зомби и вампир'])
    def test_add_new_book_not_add_two_book_with_long_and_short_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_genre_for_one_book(self, append_one_book_in_books_genre):
        append_one_book_in_books_genre.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert append_one_book_in_books_genre.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    @pytest.mark.parametrize('book_name, book_genre', [['12 стульев', 'Ужасы'], ['Гордость и предубеждение и зомби', 'Драма'], ['12 стульев', 'Приключения']])
    def test_set_book_genre_add_book_not_from_books_genre(self, append_one_book_in_books_genre, book_name, book_genre):
        append_one_book_in_books_genre.set_book_genre(book_name, book_genre)
        assert append_one_book_in_books_genre.get_book_genre(book_name) == '' or append_one_book_in_books_genre.get_book_genre(book_name) == None

    def test_get_books_with_specific_genre_for_five_book_group_by_genre(self, append_five_book_and_genre_in_books_genre):
        assert append_five_book_and_genre_in_books_genre.get_books_with_specific_genre('Комедии') == ['12 стульев', 'Золотой теленок', 'Трое в лодке'] \
               and append_five_book_and_genre_in_books_genre.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби', 'Зов Ктулху']

    def test_get_books_with_specific_genre_for_empty_book_genre(self):
        collector = BooksCollector()
        for genre in collector.genre:
            assert collector.get_books_with_specific_genre(genre) == []

    @pytest.mark.parametrize('book_genre', ['Драма', 'Фантастика'])
    def test_get_books_with_specific_genre_for_not_exist_genre_return_empty_list(self, book_genre, append_five_book_and_genre_in_books_genre):
        assert append_five_book_and_genre_in_books_genre.get_books_with_specific_genre(book_genre) == []

    def test_get_books_for_children_add_five_book_and_return_three_book_for_children(self, append_five_book_with_other_genre):
        assert append_five_book_with_other_genre.get_books_for_children() == ['12 стульев', 'Незнайка', 'Алиса в стране чудес']

    def test_get_books_for_children_genre_children_book_not_in_genre_age_rating_true(self, append_five_book_with_other_genre):
        for child_book in append_five_book_with_other_genre.get_books_for_children():
            assert append_five_book_with_other_genre.get_book_genre(child_book) not in ['Ужасы', 'Детективы']

    def test_get_books_for_children_return_empty_list(self):
        collector = BooksCollector()
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_for_two_book(self, append_five_book_with_other_genre):
        append_five_book_with_other_genre.add_book_in_favorites('12 стульев')
        append_five_book_with_other_genre.add_book_in_favorites('Зов Ктулху')
        assert append_five_book_with_other_genre.get_list_of_favorites_books() == ['12 стульев', 'Зов Ктулху']

    def test_add_book_in_favorites_for_book_not_in_books_genre(self, append_five_book_with_other_genre):
        append_five_book_with_other_genre.add_book_in_favorites('Чемодан')
        assert len(append_five_book_with_other_genre.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_one_book_twice_shows_len_of_list(self, append_five_book_with_other_genre):
        append_five_book_with_other_genre.add_book_in_favorites('12 стульев')
        append_five_book_with_other_genre.add_book_in_favorites('12 стульев')
        assert len(append_five_book_with_other_genre.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_for_two_book(self, append_three_books_in_favorite):
        append_three_books_in_favorite.delete_book_from_favorites('12 стульев')
        append_three_books_in_favorite.delete_book_from_favorites('Зов Ктулху')
        assert append_three_books_in_favorite.get_list_of_favorites_books() == ['Алиса в стране чудес']

    def test_delete_book_from_favorites_for_one_book_not_from_favorite_books(self, append_three_books_in_favorite):
        append_three_books_in_favorite.delete_book_from_favorites('Незнайка')
        assert append_three_books_in_favorite.get_list_of_favorites_books() == ['12 стульев', 'Зов Ктулху', 'Алиса в стране чудес']

    def test_delete_book_from_favorites_from_empty_favorite_books_list(self, append_five_book_with_other_genre):
        append_five_book_with_other_genre.delete_book_from_favorites('Незнайка')
        assert append_five_book_with_other_genre.get_list_of_favorites_books() == []