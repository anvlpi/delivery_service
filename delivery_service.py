def main(robots_weights, capacity_limit) -> int:
    """Функция рассчета кол-ва платформ c Методом двух указателей"""
    robots_weights.sort()
    platform_count: int = 0
    left_point: int = 0
    right_point: int = len(robots_weights) - 1
    temp_sum: int = 0

    while left_point <= right_point:
        temp_sum = robots_weights[left_point] + robots_weights[right_point]

        if left_point == right_point:
            platform_count += 1
            break
        elif (
                robots_weights[right_point] == capacity_limit or
                temp_sum > capacity_limit
        ):
            platform_count += 1
            right_point -= 1
        elif temp_sum <= capacity_limit:
            platform_count += 1
            left_point += 1
            right_point -= 1

    return platform_count


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
