"""Пример приложения для лабораторной работы №6: расчёт стоимости заказа."""


def order_total(prices, discount_percent=0):
    """Возвращает сумму заказа с учётом скидки в процентах."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть от 0 до 100 %")
    total = sum(prices)
    return round(total * (100 - discount_percent) / 100, 2)


if __name__ == "__main__":
    print("Сумма заказа:", order_total([1990, 2490, 890], 10))
