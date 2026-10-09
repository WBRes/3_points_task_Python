import math

def robot_choose(x, y, x_derivative, y_derivative, q1, q2, q1_derivative, q2_derivative):
    print("Какого робота выбираете?\n1 - цилиндр\n2 - Колер")
    chosen_r = int(input())
    print("Какую кинематическую задачу решаем?\n1 - прямую\n2 - обратную")
    chosen_t = int(input())
    print("Если хотите дефолтные значения для симуляции, введите 1, иначе что-то другое")
    custom = input()
    a1, a2 = 50.0, 50.0
    if custom != "1":
        x, y, x_derivative, y_derivative, q1, q2, q1_derivative, q2_derivative = robot_choose_logic1(chosen_t, x, y,
                                                                                                     x_derivative,
                                                                                                     y_derivative,
                                                                                                     q1, q2,
                                                                                                     q1_derivative,
                                                                                                     q2_derivative)
        if chosen_r == 1:
            a1 = float(input("Длина первого звена a1 = "))
        else:
            a2 = float(input("Длина второго звена a2 = "))
    if chosen_r == 1:
        print("\n\n\nКоординаты")
        robot_cylinder(chosen_t, a1, q1=q1, q2=q2, x=x, y=y)
        print("\n\n\nСкорости")
        robot_cylinder_velocity(chosen_t, a1=a1, q1=q1, q2=q2, q1_derivative=q1_derivative, q2_derivative=q2_derivative,
                                x=x, y=y, x_derivative=x_derivative, y_derivative=y_derivative)
    elif chosen_r == 2:
        print("\n\n\nКоординаты")
        robot_coler(chosen_t, a2, q1=q1, q2=q2, x=x, y=y)
        print("\n\n\nСкорости")
        robot_coler_velocity(chosen_t, a2=a2, q1=q1, q2=q2, q1_derivative=q1_derivative, q2_derivative=q2_derivative,
                             x=x, y=y, x_derivative=x_derivative, y_derivative=y_derivative)

def robot_choose_logic1(chosen_t, x, y, x_derivative, y_derivative, q1, q2, q1_derivative, q2_derivative):
    if chosen_t == 1:
        q1 = []
        q2 = []
        q1_derivative = []
        q2_derivative = []
        print("Введите 3 конфигурации")
        for i in range(3):
            q1.append(float(input(f"q1_{i} = ")))
            q2.append(float(input(f"q2_{i} = ")))
        print("Введите 3 скорости")
        for i in range(3):
            q1_derivative.append(float(input(f"q1_derivative{i} = ")))
            q2_derivative.append(float(input(f"q2_derivative{i} = ")))
    else:
        x = []
        y = []
        x_derivative = []
        y_derivative = []
        print("Введите координаты 3-ёх точек")
        for i in range(3):
            x.append(float(input(f"x{i} = ")))
            y.append(float(input(f"y{i} = ")))
        print("Введите 3 скорости")
        for i in range(3):
            x_derivative.append(float(input(f"x_derivative{i} = ")))
            y_derivative.append(float(input(f"y_derivative{i} = ")))
    return x, y, x_derivative, y_derivative, q1, q2, q1_derivative, q2_derivative
def robot_cylinder(chosen_t=2, a1=50,
                   q1 = [73.61045966596522, 73.61045966596522, -3.21548399174821, -79.01934998982645],
                   q2 = [-14.559909706661301, -14.559909706661301, 39.140338792266206, 18.249542123006222],
                   x=[-34, 5, 67], y=[10, 89, 13]):
    a1 = abs(a1)
    if chosen_t == 1:
        x = []
        y = []
        for i in range(len(q1)):
            print(f"Для {i + 1} конфигурации")
            q1_rad = math.radians(q1[i])
            y.append((a1 + q2[i]) * math.cos(q1_rad))
            x.append(-(a1 + q2[i]) * math.sin(q1_rad))
            print(f"x = {x[i]}")
            print(f"y = {y[i]}")
            print(f"(При q1 = {q1[i]}, q2 = {q2[i]})")
            print("=====================")
        return x, y
    elif chosen_t == 2:
        q1 = []
        q2 = []
        for i in range(len(x)):
            print(f"Для {i+1} точки")
            q1.append(math.atan2(-x[i], y[i]))
            print(f"q1 = {math.degrees(q1[i])}°")
            q2.append(((y[i])**2+(x[i])**2)**(1/2) - a1)
            print(f"q2 = {q2[i]} cm")
            print(f"(При x = {x[i]}, y = {y[i]})")
            print("=====================")
        return q1, q2

def robot_cylinder_velocity(chosen_t=2, a1=50,
                            q1 = [73.61045966596522, 73.61045966596522, -3.21548399174821, -79.01934998982645],
                            q2 = [-14.559909706661301, -14.559909706661301, 39.140338792266206, 18.249542123006222],
                            q1_derivative=[], q2_derivative=[],
                            x=[-34, 5, 67], y=[10, 89, 13], x_derivative=[], y_derivative=[]):
    a1 = abs(a1)
    if chosen_t == 1:
        y_derivative = []
        x_derivative = []
        for i in range(len(q1)):
            print(f"Для {i + 1} конфигурации")
            q1_derivative_rad = math.radians(q1_derivative[i])
            q1_rad = math.radians(q1[i])
            y_derivative.append(-(a1 + q2[i]) * math.sin(q1_rad) * q1_derivative_rad + math.cos(q1_rad) * q2_derivative[i])
            x_derivative.append(-(a1 + q2[i]) * math.cos(q1_rad) * q1_derivative_rad - math.sin(q1_rad) * q2_derivative[i])
            print(f"x_derivative = {x_derivative[i]}")
            print(f"y_derivative = {y_derivative[i]}")
            print(f"(При q1 = {q1[i]}, q2 = {q2[i]}, q1_derivative = {q1_derivative[i]}, "
                  f"q2_derivative = {q2_derivative[i]}))")
            print("=====================")
        return x_derivative, y_derivative
    elif chosen_t == 2:
        q1_derivative = []
        q2_derivative = []
        for i in range(len(x)):
            print(f"Для {i + 1} точки")
            r2 = (x[i])**2 + (y[i])**2
            r = (r2)**(1/2)
            q1_derivative.append((x[i] * y_derivative[i] - y[i] * x_derivative[i]) / r2)
            print(f"q1_derivative = {math.degrees(q1_derivative[i])}°/s")
            q2_derivative.append((x[i] * x_derivative[i] + y[i] * y_derivative[i]) / r)
            print(f"q2_derivative = {q2_derivative[i]} cm/s")
            print(f"(При x = {x[i]}, y = {y[i]}, x_derivative = {x_derivative[i]}, y_derivative = {y_derivative[i]})")
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
        for i in range(len(q1)):
            print(f"Для {i + 1} конфигурации")
            q2_rad = math.radians(q2[i])
            y.append(q1[i] + a2 * math.cos(q2_rad))
            x.append(-a2 * math.sin(q2_rad))
            print(f"x = {x[i]}")
            print(f"y = {y[i]}")
            print(f"(При q1 = {q1[i]}, q2 = {q2[i]})")
            print("=====================")
        return x, y
    elif chosen_t == 2:
        q1 = []
        q2 = []
        q1_2 = []
        q2_2 = []
        for i in range(len(x)):
            print(f"Для {i+1} точки")
            if abs(x[i]) > a2:
                print(f"При x = {x[i]}, y = {y[i]} решений нет (длина звена a2 маленькая)")
                print(f"Ближайшее решение при a2 = x{i} = {x[i]} было бы:")
                q1.append(y[i])
                q1_2.append(y[i])
                print(f"q1 = {q1[i]} cm")
                q2.append(math.radians(-90))
                q2_2.append(math.radians(-90))
                print(f"q2 = {math.degrees(q2[i])}°")
                continue
            D = (a2 ** 2 - (x[i]) ** 2) ** (1 / 2)
            print("Первое решение:")
            q1.append(y[i] - D)
            print(f"q1 = {q1[i]} cm")
            q2.append(math.asin(-x[i]/a2))
            print(f"q2 = {math.degrees(q2[i])}°")

            print("Второе решение:")
            q1_2.append(y[i] + D)
            print(f"q1 = {q1_2[i]} cm")
            q2_2.append(math.radians(180 - math.degrees(math.asin(-x[i] / a2))))
            print(f"q2 = {math.degrees(q2_2[i])}°")
            print(f"(При x = {x[i]}, y = {y[i]})")
            print("=====================")
        return q1, q2, q1_2, q2_2

def robot_coler_velocity(chosen_t=2, a2=50,
                         q1 = [73.61045966596522, 73.61045966596522, -3.21548399174821, -79.01934998982645],
                         q2 = [-14.559909706661301, -14.559909706661301, 39.140338792266206, 18.249542123006222],
                         q1_derivative=[], q2_derivative=[],
                         x=[-34, 5, 67], y=[10, 89, 13], x_derivative=[], y_derivative=[]):
    a2 = abs(a2)
    if chosen_t == 1:
        x_derivative = []
        y_derivative = []
        for i in range(len(q1)):
            print(f"Для {i + 1} конфигурации")
            q2_rad = math.radians(q2[i])
            q2_derivative_rad = math.radians(q2_derivative[i])
            y_derivative.append(q1_derivative[i] - a2 * math.sin(q2_rad) * q2_derivative_rad)
            x_derivative.append(-a2 * math.cos(q2_rad) * q2_derivative_rad)
            print(f"x_derivative = {x_derivative[i]}")
            print(f"y_derivative = {y_derivative[i]}")
            print(f"(При q1 = {q1[i]}, q2 = {q2[i]}, q1_derivative = {q1_derivative[i]}, "
                  f"q2_derivative = {q2_derivative[i]}))")
            print("=====================")
        return x_derivative, y_derivative
    elif chosen_t == 2:
        q1_derivative = []
        q2_derivative = []
        q1_2_derivative = []
        q2_2_derivative = []
        for i in range(len(x)):
            print(f"Для {i+1} точки")
            if abs(x[i]) > a2:
                print(f"При x = {x[i]}, y = {y[i]} решений нет (длина звена a2 маленькая)")
                print(f"Ближайшее решение было бы, например, при a2 = x{i}+1 = {x[i] + 1}:")
                a2_fixed = abs(x[i]) + 1
                D = (a2_fixed ** 2 - (x[i]) ** 2) ** (1 / 2)
                print("Тогда первое решение было бы:")
                q1_derivative.append(y_derivative[i] + x[i] * x_derivative[i] / D)
                print(f"q1_derivative = {q1_derivative[i]} cm/s")
                q2_derivative.append(-x_derivative[i] / D)
                print(f"q2_derivative = {math.degrees(q2_derivative[i])}°/s")
                print("А второе решение было бы:")
                q1_2_derivative.append(y_derivative[i] - x[i] * x_derivative[i] / D)
                print(f"q1_derivative = {q1_2_derivative[i]} cm/s")
                q2_2_derivative.append(x_derivative[i] / D)
                print(f"q2_derivative = {math.degrees(q2_2_derivative[i])}°/s")
                print(
                    f"(При x = {x[i]}, y = {y[i]}, x_derivative = {x_derivative[i]}, y_derivative = {y_derivative[i]})")
                print("=====================")
                continue
            elif abs(x[i]) == a2:
                print(f"Точка сингулярности при x = {x[i]}, y = {y[i]}")
                print(f"Ближайшее решение было бы, например, при a2 = x{i}+1 = {x[i] + 1}:\n")
                a2_fixed = abs(x[i]) + 1
                D = (a2_fixed ** 2 - (x[i]) ** 2) ** (1 / 2)
                print("Тогда первое решение было бы:")
                q1_derivative.append(y_derivative[i] + x[i] * x_derivative[i] / D)
                print(f"q1_derivative = {q1_derivative[i]} cm/s")
                q2_derivative.append(-x_derivative[i] / D)
                print(f"q2_derivative = {math.degrees(q2_derivative[i])}°/s")
                print("А второе решение было бы:")
                q1_2_derivative.append(y_derivative[i] - x[i] * x_derivative[i] / D)
                print(f"q1_derivative = {q1_2_derivative[i]} cm/s")
                q2_2_derivative.append(x_derivative[i] / D)
                print(f"q2_derivative = {math.degrees(q2_2_derivative[i])}°/s")
                print(
                    f"(При x = {x[i]}, y = {y[i]}, x_derivative = {x_derivative[i]}, y_derivative = {y_derivative[i]})")
                print("=====================")
                continue
            D = (a2 ** 2 - (x[i]) ** 2) ** (1 / 2)
            print("Первое решение:")
            q1_derivative.append(y_derivative[i] + x[i] * x_derivative[i] / D)
            print(f"q1_derivative = {q1_derivative[i]} cm/s")
            q2_derivative.append(-x_derivative[i] / D)
            print(f"q2_derivative = {math.degrees(q2_derivative[i])}°/s")

            print("Второе решение:")
            q1_2_derivative.append(y_derivative[i] - x[i] * x_derivative[i] / D)
            print(f"q1_derivative = {q1_2_derivative[i]} cm/s")
            q2_2_derivative.append(x_derivative[i] / D)
            print(f"q2_derivative = {math.degrees(q2_2_derivative[i])}°/s")
            print(f"(При x = {x[i]}, y = {y[i]}, x_derivative = {x_derivative[i]}, y_derivative = {y_derivative[i]})")
            print("=====================")
        return q1_derivative, q2_derivative, q1_2_derivative, q2_2_derivative

mode = input("mode: ")
x = [-34, 5, 67]
y = [10, 89, 13]
q1 = [73.61045966596522, -3.21548399174821, -79.01934998982645]
q2 = [-14.559909706661301, 39.140338792266206, 18.249542123006222]
x_derivative = [1, 2, 3]
y_derivative = [4, 5, 6]
q1_derivative = [1, 2, 3]
q2_derivative = [4, 5, 6]
a1 = 50
a2 = 50
if mode == '3_points' or mode == None or mode == "" or mode == " " or mode == "2":
    robot_choose(x=x, y=y, x_derivative=x_derivative, y_derivative=y_derivative, q1=q1, q2=q2,
                 q1_derivative=q1_derivative, q2_derivative=q2_derivative)
elif mode == "1" or mode == "skip":
    print("\n\n\nКоординаты")
    robot_cylinder(1, a1=a1, q1=q1, q2=q2, x=x, y=y)
    print("\n\n\nСкорости")
    robot_cylinder_velocity(1, a1=a1, q1=q1, q2=q2, q1_derivative=q1_derivative, q2_derivative=q2_derivative,
                            x=x, y=y, x_derivative=x_derivative, y_derivative=y_derivative)