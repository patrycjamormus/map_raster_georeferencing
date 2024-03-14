strefy = "A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-Z"
strefy_X = strefy.split("-")

def coord_x(godlo: str) -> int:
    st_x = []
    start_value = 0
    for start_value in range(0, 180, 4):
        st_x.append(start_value)
        global_zone = dict(zip(strefy_X, st_x))
    global_x = dict(zip(strefy_X, st_x))
    godlo_part = godlo.split("-")
    godlo_p = godlo_part[0][0]
    x = int((global_x.get(godlo_p)))

    strefa_2 = int(godlo_part[1])
    x += (12 - strefa_2 // 12 - 1) / 3

    if godlo_part[2] == 'A':
        x += 1 / 6
    elif godlo_part[2] == "B":
        x += 1 / 6
    if godlo_part[3] == "A,B":
        x += 1 / 12

    # if godlo_part[4] == '1' or '2':
    #     x += 1 / 24
    return x



# nr_1_30 = []
# y_1_30 = []
# 180
# nr_31_60 = []
# y_31_60 = []
# 0

def coord_y(godlo: str) -> int:
    nr_1_30 = []
    y_1_30 = []
    for n in range(1, 31, 1):
        nr_1_30.append(n)
    for n in range(31, 60, 1):
        nr_1_30.append(n)
    nr_1_30 = [str(n) for n in nr_1_30]

    for s in range(180, 355, 6):
        y_1_30.append(s)
    for s in range(0, 180, 6):
        y_1_30.append(s)
    global_y = dict(zip(nr_1_30, y_1_30))
    godlo_part = godlo.split("-")
    godlo_p = godlo_part[0][1:]
    y = int((global_y.get(godlo_p)))

    strefa_2 = int(godlo_part[1])
    y += (strefa_2 % 12 - 1) / 2
    if godlo_part[2] == "B" or "D":
        y += 1 / 4
    return y


# godlo = "M34-023-D-C,D"
# print("x=",coord_x(godlo))
# print("y=", coord_y(godlo))

def corners (x: float, y:float)-> dict:
    xld = x
    yld = y

    xlg = x + 1 / 12
    ylg = y

    xpg = xlg
    ypg = y + 1 / 4

    xpd = x
    ypd = ypg

    wynik = {"LG": (xlg, ylg),
             "LD": (xld, yld),
             "PG": (xpg, ypg),
             "PD": (xpd, ypd)}

    return wynik

godlo = "M34-023-D-C,D"
print(corners(x=coord_x(godlo), y=coord_y(godlo)))

