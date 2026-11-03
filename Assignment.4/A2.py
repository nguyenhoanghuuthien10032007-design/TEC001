import re
def check_hexadecimal_color(color: str) -> bool:
    pattern = r"^#[0-9A-Fa-f]{6}$"
    return bool(re.match(pattern, color))
print(check_hexadecimal_color("#TVY038"))
print(check_hexadecimal_color("#HTH103"))
print(check_hexadecimal_color("#ABC000"))
