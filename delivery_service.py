# ID успешной посылки: 161773423
def calc_platform_count(robots_weights: list[int], capacity_limit: int) -> int:
    """Расчитать кол-во платформ для размещения роботов Методом двух указателей

    Args:
        robots_weights (list[int]): Список весов роботов
        capacity_limit (int): Максимальный вес роботов для одной платформы

    Returns:
        int: Возвращает минимальное количество платформ для перевозки
            робототов из параметра robots_weights
    """
    robots_weights.sort()
    platforms_count = 0
    left_point = 0
    right_point = len(robots_weights) - 1
    weight_temp_sum = 0

    while left_point <= right_point:
        weight_temp_sum = (
                            robots_weights[left_point] +
                            robots_weights[right_point]
        )
        platforms_count += 1

        # Если указатели соприкоснулись - проверять не чего,
        # просто добавляем платформы и прерываем
        if left_point == right_point:
            break
        # Если правый указатель с весом = грузоподъемности
        # или вес слишком большой
        elif (
                robots_weights[right_point] == capacity_limit or
                weight_temp_sum > capacity_limit
        ):
            right_point -= 1
        # Если вес именно двух указателей меньше или равен,
        # значит добавляем платформы
        elif weight_temp_sum <= capacity_limit:
            left_point += 1
            right_point -= 1

    return platforms_count


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        robots_weights: list[int] = [
                                        int(weight) for weight
                                        in file.readline().split(' ')
                                    ]
        capacity_limit: int = int(file.readline())
    result = calc_platform_count(robots_weights, capacity_limit)
    with open('output.txt', 'w') as file:
        file.write(str(result))
