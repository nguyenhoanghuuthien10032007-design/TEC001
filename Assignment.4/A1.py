import re
def check_course_code(code: str) -> bool:
    pattern = r"^[A-Z]{3}\d{3}$"
    return bool(re.match(pattern, code))
print(check_course_code("TEC001"))
print(check_course_code("tec001"))
print(check_course_code("TEC112"))