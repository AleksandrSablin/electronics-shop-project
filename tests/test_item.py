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
