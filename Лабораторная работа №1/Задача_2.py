# TODO Найдите количество книг, которое можно разместить на дискете
size_in_mb = 1.44
pages = 100
str = 50
sym = 25
need_in_b = 4

full_in_b = need_in_b * sym * str * pages
full_in_mb = full_in_b / (1024**2)

count = size_in_mb / full_in_mb
print(f"Количество книг, помещающихся на дискету: {count:.0f}")
