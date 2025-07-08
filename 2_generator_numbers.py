import re
from typing import Callable
from decimal import Decimal

REAL_NUMBER_PATTERN = r"\s?([+-]?\d*\.?\d+)\s?"


def generator_numbers(text: str):
    for number in re.findall(REAL_NUMBER_PATTERN, text):
        yield Decimal(number)


def sum_profit(text: str, func: Callable):
    sum = Decimal(0.0)

    for profit in func(text):
        sum += profit

    return sum


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  # 1351.46

    text2 = "0.002 0.2 2 1 2.00 2. 2.000 -3 -0.05 0 33.45 "
    total_income2 = sum_profit(text2, generator_numbers)
    print(f"Загальний дохід: {total_income2}")  # 39.602


if __name__ == "__main__":
    main()
