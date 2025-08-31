from typing import Iterator, Callable

def generator_numbers(text:str)->Iterator[float]:
    for word in text.split()[1: -1]:
        try:
            num = float(word)
            yield num
        except ValueError:
            continue


def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "134 Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
