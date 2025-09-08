choice = input("选 1 摄氏→华氏，选 2 华氏→摄氏：")
if choice == "1":
    c = float(input("摄氏温度："))
    f = c * 9/5 + 32
    print(f"{c}°C = {f:.1f}°F")
elif choice == "2":
    f = float(input("华氏温度："))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c:.1f}°C")
else:
    print("只能输入 1 或 2")