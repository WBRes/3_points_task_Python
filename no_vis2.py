import math

def robot_choose(x, y, q1, q2, t=10.0):
    print("Какого робота выбираете?\n1 - цилиндр\n2 - Колер")
    chosen_r = int(input())
    print("Какую кинематическую задачу решаем?\n1 - прямую\n2 - обратную")
    chosen_t = int(input())
    print("Если хотите дефолтные значения для симуляции, введите 0, иначе что-то другое")
    custom = input()
    a1, a2 = 50.0, 50.0
    if custom == "0":
        x, y, q1, q2 = robot_choose_logic1(chosen_t, x, y, q1, q2)
        if chosen_r == 1:
            a1 = float(input("Длина первого звена a1 = "))
        else:
            a2 = float(input("Длина второго звена a2 = "))
    if chosen_r == 1:
        print("\n\n\nКоординаты")
        robot_cylinder(chosen_t, a1, q1=q1, q2=q2, x=x, y=y)
        print("\n\n\nСкорости")
        robot_cylinder_velocity(chosen_t, a1, q1=q1, q2=q2, x=x, y=y, t=t)
    elif chosen_r == 2:
        print("\n\n\nКоординаты")
        robot_coler(chosen_t, a2, q1=q1, q2=q2, x=x, y=y)
        print("\n\n\nСкорости")
        robot_coler_velocity(chosen_t, a2, q1=q1, q2=q2, x=x, y=y, t=t)

def robot_choose_logic1(chosen_t, x, y, q1, q2):
    if chosen_t == 1:
        q1 = []
        q2 = []
        print("Введите 4 конфигурации (Дополнительная 0-ая конфигурация описывает начальное положение робота)")
        for i in range(4):
            q1.append(float(input(f"q1_{i} = ")))
            q2.append(float(input(f"q2_{i} = ")))
    else:
        x = []
        y = []
        print("Введите координаты 4-ёх точек (Дополнительная 0-ая точка описывает начальное положение робота)")
        for i in range(4):
            x.append(float(input(f"x{i} = ")))
            y.append(float(input(f"y{i} = ")))
    return x, y, q1, q2
def robot_cylinder(chosen_t=2, a1=50,
                   q1 = [73.61045966596522, 73.61045966596522, -3.21548399174821, -79.01934998982645],
                   q2 = [-14.559909706661301, -14.559909706661301, 39.140338792266206, 18.249542123006222],
                   x=[-34, 5, 67], y=[10, 89, 13]):
    a1 = abs(a1)
    if chosen_t == 1:
        x = []
        y = []
        for i in range(len(q1)-1):
            print(f"Для {i + 1} конфигурации")
            q1_rad = math.radians(q1[i+1])
            y.append((a1 + q2[i+1]) * math.cos(q1_rad))
            x.append(-(a1 + q2[i+1]) * math.sin(q1_rad))
            print(f"x = {x[i]}")
            print(f"y = {y[i]}")
            print(f"(При q1 = {q1[i+1]}, q2 = {q2[i+1]})")
            print("=====================")
        return x, y
    elif chosen_t == 2:
        q1 = []
        q2 = []
        for i in range(len(x)-1):
            print(f"Для {i+1} точки")
            q1.append(math.atan2(-x[i+1], y[i+1]))
            print(f"q1 = {math.degrees(q1[i])}°")
            q2.append(((y[i+1])**2+(x[i+1])**2)**(1/2) - a1)
            print(f"q2 = {q2[i]} cm")
            print(f"(При x = {x[i+1]}, y = {y[i+1]})")
            print("=====================")
        return q1, q2

def robot_cylinder_velocity(chosen_t=2, a1=50,
                            q1 = [73.61045966596522, 73.61045966596522, -3.21548399174821, -79.01934998982645],
                            q2 = [-14.559909706661301, -14.559909706661301, 39.140338792266206, 18.249542123006222],
                            x=[-34, 5, 67], y=[10, 89, 13], t = 10.0):
    a1 = abs(a1)
    if chosen_t == 1:
        y_derivative = []
        x_derivative = []
        for i in range(len(q1)-1):
            print(f"Для {i + 1} конфигурации")
            q1_derivative, q2_derivative = calculate_derivative(i, q1, q2, t)
            q1_derivative_rad = math.radians(q1_derivative)
            q1_rad = math.radians(q1[i+1])
            y_derivative.append(-(a1 + q2[i+1]) * math.sin(q1_rad) * q1_derivative_rad + math.cos(q1_rad) * q2_derivative)
            x_derivative.append(-(a1 + q2[i+1]) * math.cos(q1_rad) * q1_derivative_rad - math.sin(q1_rad) * q2_derivative)
            print(f"x_derivative = {x_derivative[i]}")
            print(f"y_derivative = {y_derivative[i]}")
            print(f"(При q1 = {q1[i + 1]}, q2 = {q2[i + 1]}, q1_derivative = {q1_derivative}, "
                  f"q2_derivative = {q2_derivative}))")
            print("=====================")
        return x_derivative, y_derivative
    elif chosen_t == 2:
        q1_derivative = []
        q2_derivative = []
        for i in range(len(x)-1):
            x_derivative, y_derivative = calculate_derivative(i, x, y, t)
            print(f"Для {i + 1} точки")
            r2 = (x[i+1])**2 + (y[i+1])**2
            r = (r2)**(1/2)
            q1_derivative.append((x[i+1] * y_derivative - y[i+1] * x_derivative) / r2)
            print(f"q1_derivative = {math.degrees(q1_derivative[i])}°/s")
            q2_derivative.append((x[i+1] * x_derivative + y[i+1] * y_derivative) / r)
            print(f"q2_derivative = {q2_derivative[i]} cm/s")
            print(f"(При x = {x[i+1]}, y = {y[i+1]}, x_derivative = {x_derivative}, y_derivative = {y_derivative})")
            print("=====================")
        return q1_derivative, q2_derivative


def robot_coler(chosen_t=2, a2=50,
                q1 = [73.61045966596522, 73.61045966596522, -3.21548399174821, -79.01934998982645],
                q2 = [-14.559909706661301, -14.559909706661301, 39.140338792266206, 18.249542123006222],
                x=[-34, 5, 67], y=[10, 89, 13]):
    a2 = abs(a2)
    if chosen_t == 1:
        x = []
        y = []
        for i in range(len(q1)-1):
            print(f"Для {i + 1} конфигурации")
            q2_rad = math.radians(q2[i+1])
            y.append(q1[i+1] + a2 * math.cos(q2_rad))
            x.append(-a2 * math.sin(q2_rad))
            print(f"x = {x[i]}")
            print(f"y = {y[i]}")
            print(f"(При q1 = {q1[i + 1]}, q2 = {q2[i + 1]})")
            print("=====================")
        return x, y
    elif chosen_t == 2:
        q1 = []
        q2 = []
        q1_2 = []
        q2_2 = []
        for i in range(len(x)-1):
            print(f"Для {i+1} точки")
            if abs(x[i+1]) > a2:
                print(f"При x = {x[i+1]}, y = {y[i+1]} решений нет (длина звена a2 маленькая)")
                print(f"Ближайшее решение при a2 = x{i+1} = {x[i+1]} было бы:")
                q1.append(y[i+1])
                q1_2.append(y[i+1])
                print(f"q1 = {q1[i]} cm")
                q2.append(math.radians(-90))
                q2_2.append(math.radians(-90))
                print(f"q2 = {math.degrees(q2[i])}°")
                continue
            D = (a2 ** 2 - (x[i+1]) ** 2) ** (1 / 2)
            print("Первое решение:")
            q1.append(y[i+1] - D)
            print(f"q1 = {q1[i]} cm")
            q2.append(math.asin(-x[i+1]/a2))
            print(f"q2 = {math.degrees(q2[i])}°")

            print("Второе решение:")
            q1_2.append(y[i+1] + D)
            print(f"q1 = {q1_2[i]} cm")
            q2_2.append(math.radians(180 - math.degrees(math.asin(-x[i+1] / a2))))
            print(f"q2 = {math.degrees(q2_2[i])}°")
            print(f"(При x = {x[i+1]}, y = {y[i+1]})")
            print("=====================")
        return q1, q2, q1_2, q2_2

def robot_coler_velocity(chosen_t=2, a2=50,
                         q1 = [73.61045966596522, 73.61045966596522, -3.21548399174821, -79.01934998982645],
                         q2 = [-14.559909706661301, -14.559909706661301, 39.140338792266206, 18.249542123006222],
                         x=[-34, 5, 67], y=[10, 89, 13], t=10.0):
    a2 = abs(a2)
    if chosen_t == 1:
        x_derivative = []
        y_derivative = []
        for i in range(len(q1) - 1):
            print(f"Для {i + 1} конфигурации")
            q2_rad = math.radians(q2[i+1])
            q1_derivative, q2_derivative = calculate_derivative(i, q1, q2, t)
            q2_derivative_rad = math.radians(q2_derivative)
            y_derivative.append(q1_derivative - a2 * math.sin(q2_rad) * q2_derivative_rad)
            x_derivative.append(-a2 * math.cos(q2_rad) * q2_derivative_rad)
            print(f"x_derivative = {x_derivative[i]}")
            print(f"y_derivative = {y_derivative[i]}")
            print(f"(При q1 = {q1[i + 1]}, q2 = {q2[i + 1]}, q1_derivative = {q1_derivative}, "
                  f"q2_derivative = {q2_derivative}))")
            print("=====================")
        return x_derivative, y_derivative
    elif chosen_t == 2:
        q1_derivative = []
        q2_derivative = []
        q1_2_derivative = []
        q2_2_derivative = []
        for i in range(len(x)-1):
            x_derivative, y_derivative = calculate_derivative(i, x, y, t)
            print(f"Для {i+1} точки")
            if abs(x[i+1]) > a2:
                print(f"При x = {x[i+1]}, y = {y[i+1]} решений нет (длина звена a2 маленькая)")
                print(f"Ближайшее решение было бы, например, при a2 = x{i + 1}+1 = {x[i+1] + 1}:")
                a2_fixed = abs(x[i+1]) + 1
                D = (a2_fixed ** 2 - (x[i+1]) ** 2) ** (1 / 2)
                print("Тогда первое решение было бы:")
                q1_derivative.append(y_derivative + x[i+1] * x_derivative / D)
                print(f"q1_derivative = {q1_derivative[i]} cm/s")
                q2_derivative.append(-x_derivative / D)
                print(f"q2_derivative = {math.degrees(q2_derivative[i])}°/s")
                print("А второе решение было бы:")
                q1_2_derivative.append(y_derivative - x[i+1] * x_derivative / D)
                print(f"q1_derivative = {q1_2_derivative[i]} cm/s")
                q2_2_derivative.append(x_derivative / D)
                print(f"q2_derivative = {math.degrees(q2_2_derivative[i])}°/s")
                print(
                    f"(При x = {x[i+1]}, y = {y[i+1]}, x_derivative = {x_derivative}, y_derivative = {y_derivative})")
                print("=====================")
                continue
            elif abs(x[i+1]) == a2:
                print(f"Точка сингулярности при x = {x[i+1]}, y = {y[i+1]}")
                print(f"Ближайшее решение было бы, например, при a2 = x{i + 1}+1 = {x[i+1] + 1}:\n")
                a2_fixed = abs(x[i+1]) + 1
                D = (a2_fixed ** 2 - (x[i+1]) ** 2) ** (1 / 2)
                print("Тогда первое решение было бы:")
                q1_derivative.append(y_derivative + x[i+1] * x_derivative / D)
                print(f"q1_derivative = {q1_derivative[i]} cm/s")
                q2_derivative.append(-x_derivative / D)
                print(f"q2_derivative = {math.degrees(q2_derivative[i])}°/s")
                print("А второе решение было бы:")
                q1_2_derivative.append(y_derivative - x[i+1] * x_derivative / D)
                print(f"q1_derivative = {q1_2_derivative[i]} cm/s")
                q2_2_derivative.append(x_derivative / D)
                print(f"q2_derivative = {math.degrees(q2_2_derivative[i])}°/s")
                print(
                    f"(При x = {x[i+1]}, y = {y[i+1]}, x_derivative = {x_derivative}, y_derivative = {y_derivative})")
                print("=====================")
                continue
            D = (a2 ** 2 - (x[i+1]) ** 2) ** (1 / 2)
            print("Первое решение:")
            q1_derivative.append(y_derivative + x[i+1] * x_derivative / D)
            print(f"q1_derivative = {q1_derivative[i]} cm/s")
            q2_derivative.append(-x_derivative / D)
            print(f"q2_derivative = {math.degrees(q2_derivative[i])}°/s")

            print("Второе решение:")
            q1_2_derivative.append(y_derivative - x[i+1] * x_derivative / D)
            print(f"q1_derivative = {q1_2_derivative[i]} cm/s")
            q2_2_derivative.append(x_derivative / D)
            print(f"q2_derivative = {math.degrees(q2_2_derivative[i])}°/s")
            print(f"(При x = {x[i+1]}, y = {y[i+1]}, x_derivative = {x_derivative}, y_derivative = {y_derivative})")
            print("=====================")
        return q1_derivative, q2_derivative, q1_2_derivative, q2_2_derivative

def calculate_derivative(i, f, s, t=10.0):
    dt = t / (min(len(f), len(s)) - 1)
    f_derivative = (f[i + 1] - f[i]) / dt
    s_derivative = (s[i + 1] - s[i]) / dt
    return f_derivative, s_derivative

mode = input("mode: ")
x = [0, -34, 5, 67]
y = [50, 10, 89, 13]
q1 = [0.0, 73.61045966596522, -3.21548399174821, -79.01934998982645]
q2 = [0.0, -14.559909706661301, 39.140338792266206, 18.249542123006222]
a1 = 50
a2 = 50
if mode == '3_points' or mode == None or mode == "" or mode == " " or mode == "2":
    robot_choose(x=x, y=y, q1=q1, q2=q2, t=10.0)
elif mode == "1" or mode == "skip":
    print("\n\n\nКоординаты")
    robot_cylinder(1, a1=a1, q1=q1, q2=q2, x=x, y=y)
    print("\n\n\nСкорости")
    robot_cylinder_velocity(1, a1=a1, q1=q1, q2=q2, x=x, y=y, t=10.0)


