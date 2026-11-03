import re
def sum_numbers_in_text(text: str) -> int:
    numbers = re.findall(r"\d+", text)
    return sum(int(n) for n in numbers)
text = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
print(sum_numbers_in_text(text))  