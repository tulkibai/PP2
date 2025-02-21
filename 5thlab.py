import re

def f1(s):
    return bool(re.fullmatch(r"ab*", s))

def f2(s):
    return bool(re.fullmatch(r"ab{2,3}", s))

def f3(s):
    return re.findall(r"[a-z]+_[a-z]+", s)

def f4(s):
    return re.findall(r"[A-Z][a-z]+", s)

def f5(s):
    return bool(re.fullmatch(r"a.*b", s))

def f6(s):
    return re.sub(r"[ ,.]", ":", s)

def f7(s):
    return "".join(word.capitalize() for word in s.split("_"))

def f8(s):
    return re.split(r"(?=[A-Z])", s)

def f9(s):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", s)

def f10(s):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", s).lower()

import re

data = open("row.txt", "r")

bin_match = re.search(r"БИН (\d+)", data)
bin_number = bin_match.group(1) if bin_match else None
date_match = re.search(r"Время: ([\d.]+) (\d+:\d+:\d+)", data)
date_time = f"{date_match.group(1)} {date_match.group(2)}" if date_match else None
total_match = re.search(r"ИТОГО:\s*([\d\s,]+)", data)
total = total_match.group(1).strip() if total_match else None
items = re.findall(r"\d+\.\n(.*?)\n\d+,\d+", data)

print(f"БИН: {bin_number}")
print(f"Дата и время: {date_time}")
print(f"ИТОГО: {total}")
print("Товары:")
for item in items:
    print(f"- {item}")