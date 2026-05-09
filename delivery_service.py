# ID успешной посылки: 161756950
def main(robots_weights, capacity_limit) -> int:
    """Функция рассчета кол-ва платформ c Методом двух указателей"""
    robots_weights.sort()
    platforms_count: int = 0
    left_point: int = 0
    right_point: int = len(robots_weights) - 1
    weight_temp_sum: int = 0

    while left_point <= right_point:
        weight_temp_sum = (
                            robots_weights[left_point] +
                            robots_weights[right_point]
        )

        # Если указатели соприкоснулись - проверять не чего,
        # просто добавляем платформы и прерываем
        if left_point == right_point:
            platforms_count += 1
            break
        # Если правый указатель с весом = грузоподъемности
        # или вес слишком большой
        elif (
                robots_weights[right_point] == capacity_limit or
                weight_temp_sum > capacity_limit
        ):
            platforms_count += 1
            right_point -= 1
        # Если вес именно двух указателей меньше или равен,
        # значит добавляем платформы
        elif weight_temp_sum <= capacity_limit:
            platforms_count += 1
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
    result = main(robots_weights, capacity_limit)
    with open('output.txt', 'w') as file:
        file.write(str(result))
