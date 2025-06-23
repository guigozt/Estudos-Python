def venceJogo(pulo, canos):
    i = 0
    while i < len(canos)-1:
        if abs(canos[i] > canos[i+1]) > pulo:
            return False
        i += 1
    return True

def main():
    pulo, qtdCanos = map(int, input().split())

    canos = list(map(int, input().split()))

    if venceJogo(pulo, canos):
        print('YOU WIN')
    else:
        print('GAME OVER')

main()
