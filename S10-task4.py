customer=[
    ("alex","vip"),
    ("bob","regular"),
    ("sarah","regular"),
    ("maria","vip"),
    ("mike","regular")
]
for name,status in customer:
    if status=="vip":
        print(name)
for name,status in customer:
    if status=="regular":
        print(name)