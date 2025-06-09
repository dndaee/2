A = float(input("Введіть щомісячну стипендію (грн): "))
B = float(input("Введіть щомісячні витрати на початку (грн): "))

total_needed_from_parents = 0
current_expenses = B

for month in range(1, 11):
    shortage = current_expenses - A
    total_needed_from_parents += shortage
    current_expenses *= 1.05 

print(f"Сума, яку потрібно попросити в батьків: {total_needed_from_parents:.2f} грн")
