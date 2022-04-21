a = "         "

print(f"---------\n| {a[0]} {a[1]} {a[2]} |\n| {a[3]} {a[4]} {a[5]} |\n| {a[6]} {a[7]} {a[8]} |\n---------")

x_counter = 0
o_counter = 0

while True:

    def winner(who):
        if a[0] == a[4] == a[8] == who:
            return True
        elif a[2] == a[4] == a[6] == who:
            return True
        matrix_h = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]
        matrix_v = [[a[0], a[3], a[6]], [a[1], a[4], a[7]], [a[2], a[5], a[8]]]
        for i in range(0, 3):
            if matrix_h[i].count(who) == 3:
                return True
        for i in range(0, 3):
            if matrix_v[i].count(who) == 3:
                return True

    q, w = input("Enter the coordinates: ").split()
    a_list = list(a)
    if not q.isdigit() or not w.isdigit():
        print("You should enter numbers!")
        continue
    row = int(q)
    column = int(w)
    if column > 3 or row > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    index = (((row - 1) * 3) + (column + 2)) - 3

    if a_list[index] == " ":
        if x_counter == o_counter:
            a_list[index] = "X"
            x_counter += 1
        else:
            a_list[index] = "O"
            o_counter += 1
        a = "".join(a_list)
        print(f"---------\n| {a[0]} {a[1]} {a[2]} |\n| {a[3]} {a[4]} {a[5]} |\n| {a[6]} {a[7]} {a[8]} |\n---------")
        x_wins = 0
        o_wins = 0
        if winner('X'):
            x_wins += 1
        if winner('O'):
            o_wins += 1
        if x_wins == 1 and o_wins == 1:
            print('Impossible')
            break
        elif x_wins == 1 and o_wins != 1:
            print("X wins")
            break
        elif x_wins != 1 and o_wins == 1:
            print("O wins")
            break
        elif a.count(" ") == 0:
            print("Draw")
            break
        else:
            continue
    else:
        print("This cell is occupied! Choose another one!")

