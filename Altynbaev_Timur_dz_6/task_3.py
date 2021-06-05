
with open("users.csv", "r", encoding="utf-8") as users:
    content_users = users.read().splitlines()
    print(content_users)

with open("hobby.csv", "r", encoding="utf-8") as hobby:
    content_hobby = hobby.read().splitlines()
    print(content_hobby)

dicts = dict(zip(content_users, content_hobby))
print(dicts)

with open("user-hobby.txt", "w", encoding="utf-8") as mix:
    content = mix.writelines(f"{dicts}")