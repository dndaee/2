import math

alpha_deg = float(input("Введіть значення кута α (у градусах): "))

alpha_rad = math.radians(alpha_deg)

cos_alpha = math.cos(alpha_rad)
z = cos_alpha**2 + cos_alpha**4

print(f"Результат: z = {z:.4f}")
