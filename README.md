# qa_python
Тесты, покрывающие класс, метод __init__:
test_books_genre_of_books_collector_true  #проверяет то, что значение переменной books_genre класса BooksCollector соответствует пустому словарю
test_favorites_of_books_collector_true #проверяет то, что значение переменной favorites класса BooksCollector соответствует пустому списку
test_genre_of_books_collector_true #проверяет то, что значение переменной genre класса BooksCollector соответствует списку ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
test_genre_age_rating_of_books_collector_true #проверяет то, что значение переменной genre_age_rating класса BooksCollector соответствует списку ['Ужасы', 'Детективы']

Тесты, покрывающие метод add_new_book
test_add_new_book_add_two_books_shows_len_of_dict #добавляет две книги в books_genre, проверяет то, что длина books_genre после добавления = 2
test_add_new_book_add_two_books_in_books_genre_shows_elements_of_dict #добавляет две книги в books_genre, проверяет, что оба добавленных элемента присутствуют в books_genre
test_add_new_book_add_one_book_shows_genre_is_empty #добавляет одну книгу в books_genre, проверяет то, что для нее установлен жанр = ''
test_add_new_book_add_one_book_twice_shows_len_of_list #добавляет дважды книгу с одним названиием в books_genre, проверяет, что длина books_genre после добавления = 1
test_add_new_book_not_add_two_book_with_long_and_short_name #использует параметризацию, передает в параметр book_name название меньше требуемое длины и название больше требуемой длины, проверяет то, что оба названия не добавлены в books_genre, длина books_genre = 0

Тесты, покрывающие метод set_book_genre
#для обоих тестов используется фикстура append_one_book_in_books_genre, которая создает объект класса и добавляет 1 книгу в books_genre
test_set_book_genre_add_genre_for_one_book #позитивный тест-кейс, устанавливает книге из books_genre жанр из genre, проверяет то, что жанр соответствует установленному, используя метод get_book_genre
test_set_book_genre_add_book_not_from_books_genre #негативный тест_кейс, использует параметризацию, передает в параметры 'book_name, book_genre' комбинации: наименование отсутствует в books_genre + жанр присутствует в genre, наименование отсутствует в books_genre + жанр отсутствует в genre, проверяет, что во всех случаях жанр не был установлен
test_set_book_genre_add_book_not_from_genre #негативный тест_кейс, добавляет комбинацию - наименование присутствует в books_genre + жанр отсутствует в genre, проверяет, что жанр не был установлен

Тесты, покрывающие метод get_book_genre
При тестированиии метода set_book_genre ожидаемый результат проверяется вызовом метода get_book_genre, такиим образом тесты для set_book_genre покрывают также get_book_genre

Тесты, покрывающие метод get_books_with_specific_genre
test_get_books_with_specific_genre_for_five_book_group_by_genre #позитивный тест_кейс, фикстурой append_five_book_and_genre_in_books_genre в books_genre предварительно добавляются 5 книг с разными жанрами, метод проверяет, что книги сгруппировались согласно установленным жанрами
test_get_books_with_specific_genre_for_empty_book_genre #негативный тест-кейс, проверяет возврат пустого списка в случае, когда на момент тестирования books_genre пуст
test_get_books_with_specific_genre_for_not_exist_genre_return_empty_list #негативный тест-кейс, фикстурой append_five_book_and_genre_in_books_genre в books_genre предварительно добавляются 5 книг с разными жанрами, с помощью параметризации проверяется, что метод вернет пустые списки, если задан жанр, отсутствующий в genre или в books_genre

Тесты, покрывающие метод get_books_genre
При тестированиии метода add_new_book ожидаемый результат проверяется вызовом метода get_books_genre, такиим образом тесты для add_new_book покрывают также get_books_genre

Тесты, покрывающие метод get_books_for_children
test_get_books_for_children_add_five_book_and_return_three_book_for_children #позитивный тест_кейс, фикстурой append_five_book_with_other_genre в books_genre предварительно добавляются 5 книг с разными жанрами, проверяет, что три из них попали в список для детей
test_get_books_for_children_genre_children_book_not_in_genre_age_rating_true #фикстурой append_five_book_with_other_genre в books_genre предварительно добавляются 5 книг с разными жанрами, проверяет, что жанры книг, попавшие в список для детей, не соответствуют жанрам из списка genre_age_rating
test_get_books_for_children_return_empty_list #проверяет, что get_books_for_children возвращает пустой список,ю если в books_genre отсутствуют записи

Тесты, покрывающие метод add_book_in_favorites
test_add_book_in_favorites_for_two_book - #позитивный тест_кейс, фикстурой append_five_book_with_other_genre в books_genre предварительно добавляются 5 книг с разными жанрами, добавляет две книги в favorites, проверяет, что список favorites содержит обе книги
test_add_book_in_favorites_for_book_not_in_books_genre - #негативный тест_кейс, фикстурой append_five_book_with_other_genre в books_genre предварительно добавляются 5 книг с разными жанрами, в favorites добавляется книга, название которой отстутствует в books_genre, проверяет, что favorites остался пуст
test_add_book_in_favorites_add_one_book_twice_shows_len_of_list - #фикстурой append_five_book_with_other_genre в books_genre предварительно добавляются 5 книг с разными жанрами, в favorites добавляется дважды книга с одним названием, проверяет, что после добавления длина get_list_of_favorites_books = 1

Тесты, покрывающие метод delete_book_from_favorites
test_delete_book_from_favorites_for_two_book - #позитивный тест_кейс, фикстурой append_three_books_in_favorite в books_genre предварительно добавляются 5 книг с разными жанрами и 2 книги добавляются в favorites, методом delete_book_from_favorites 1 книга удаляется из favorites, проверяется, что favorites содержит 1 книгу, которая не была удалена
test_delete_book_from_favorites_for_one_book_not_from_favorite_books - #негативный тест_кейс, фикстурой append_three_books_in_favorite в books_genre предварительно добавляются 5 книг с разными жанрами и 2 книги добавляются в favorites, методом delete_book_from_favorites удаляется книга, которая отсутствует в favorites, проверяется, что список favorites содержит все 2 книги
test_delete_book_from_favorites_from_empty_favorite_books_list - #негативный тест_кейс, фикстурой append_five_book_with_other_genre в books_genre предварительно добавляются 5 книг с разными жанрами, ничего не добавляется в favorites,  методом delete_book_from_favorites удаляется книга, которая отсутствует в favorites, проверяется, что список favorites остался пуст

Тесты, покрывающиие метод get_list_of_favorites_books
При тестированиии метода delete_book_from_favorites ожидаемый результат проверяется вызовом метода get_list_of_favorites_books, таким образом тесты для delete_book_from_favorites покрывают также get_list_of_favorites_books