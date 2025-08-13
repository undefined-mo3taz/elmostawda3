signups=[
    ("liam", "science"),
    ("emma","art"),
    ("olivia","science"),
    ("liam","art"),
    ("noah","art"),
    ("emma","science")
]
x=set()
science_club=set()
art_club=set()
for name,club in signups:
    if name not in x:
        x.add(name)
        if club=="science":
            science_club.add(name)
        else:
            art_club.add(name)
print(f"science club{science_club}")
print(f"art club{art_club}")