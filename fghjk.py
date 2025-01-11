result = []
g = []
def divider(a, b):
    if a < b:
        raise ValueError("ValueError")
    if b > 100:
        raise IndexError("IndexError")
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, "[]": 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        g.append(f"{key} нельзя поделить на {data[key]} потому чтo {e}")

print(f"Исключения: {g}")
print(f"Результаты: {result}")