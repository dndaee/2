from finance_module import calculate_parent_support

A = float(input("Введіть щомісячну стипендію (грн): "))
B = float(input("Введіть щомісячні витрати на початку (грн): "))

total_needed = calculate_parent_support(A, B)

print(f"Сума, яку потрібно попросити в батьків: {total_needed:.2f} грн")
