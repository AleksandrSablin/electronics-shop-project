from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_item_init():
    item = Item("Смартфон", 10000, 20)
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20
    assert len(item.all) == 1


def test_item_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    item.apply_discount()
    assert item.price == 10000

    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000

    """Запускаем метод вызывающий класс из файла"""
    Item.instantiate_from_csv()
    """Проверяем корректность работы метода, подсчетом записей"""
    assert len(Item.all) == 5

    item6 = Item.all[0]
    assert item6.name == 'Смартфон'

    """проверка стаческого метода, который возвращает число из числа-строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

    # Проверяем магический метод __repr__
    assert repr(item) == "Item('Смартфон', 8000.0, 20)"

    # Проверяем магический метод __str__
    assert str(item) == 'Смартфон'