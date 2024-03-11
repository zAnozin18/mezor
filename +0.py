def win():
    if arena[0][0] == 'x' and arena[0][1] == 'x' and arena[0][2] == 'x':
        return 'x'
    if arena[1][0] == 'x' and arena[1][1] == 'x' and arena[1][2] == 'x':
        return 'x'
    if arena[2][0] == 'x' and arena[2][1] == 'x' and arena[2][2] == 'x':
        return 'x'
    if arena[0][0] == 'x' and arena[1][1] == 'x' and arena[2][2] == 'x':
        return 'x'
    if arena[2][0] == 'x' and arena[1][1] == 'x' and arena[0][2] == 'x':
        return 'x'
    if arena[0][0] == 'x' and arena[1][0] == 'x' and arena[2][0] == 'x':
        return 'x'
    if arena[0][1] == 'x' and arena[1][1] == 'x' and arena[2][1] == 'x':
        return 'x'
    if arena[0][2] == 'x' and arena[1][2] == 'x' and arena[2][2] == 'x':
        return 'x'

    if arena[0][0] == '0' and arena[0][1] == '0' and arena[0][2] == '0':
        return '0'
    if arena[1][0] == '0' and arena[1][1] == '0' and arena[1][2] == '0':
        return '0'
    if arena[2][0] == '0' and arena[2][1] == '0' and arena[2][2] == '0':
        return '0'
    if arena[0][0] == '0' and arena[1][1] == '0' and arena[2][2] == '0':
        return '0'
    if arena[2][0] == '0' and arena[1][1] == '0' and arena[0][2] == '0':
        return '0'
    if arena[0][0] == '0' and arena[1][0] == '0' and arena[2][0] == '0':
        return '0'
    if arena[0][1] == '0' and arena[1][1] == '0' and arena[2][1] == '0':
        return '0'
    if arena[0][2] == '0' and arena[1][2] == '0' and arena[2][2] == '0':
        return '0'

    return '*'


arena = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

for hod in range(1, 10):
    x0 = int(input('stroka')) - 1
    x1 = int(input('line')) - 1
    a = ''
    print(hod)
    if hod % 2 == 0:
        a = 'x'
        print('krestiki')

    else:
        a = '0'
        print('noliki')
    if arena[x0][x1] == '*':
        arena[x0][x1] = a
    else:
        print('NELZYA')
        if hod > 8:
            print('Nichya')
    for x in arena:
        print(x)

    if win() == 'x':
        print('X wins')
        break
    elif win() == '0':
        print('0 wins')
        break
