def generate_spiral_square(n):
    matrix = [[0] * n for _ in range(n)]
    direction = 0  # 0: derecha, 1: abajo, 2: izquierda, 3: arriba
    x, y = 0, 0
    num = 1

    for _ in range(1, n * n + 1):
        matrix[y][x] = num
        num += 1

        if direction == 0:
            if x + 1 < n and matrix[y][x + 1] == 0:
                x += 1
            else:
                direction = 1
                y += 1
        elif direction == 1:
            if y + 1 < n and matrix[y + 1][x] == 0:
                y += 1
            else:
                direction = 2
                x -= 1
        elif direction == 2:
            if x - 1 >= 0 and matrix[y][x - 1] == 0:
                x -= 1
            else:
                direction = 3
                y -= 1
        elif direction == 3:
            if y - 1 >= 0 and matrix[y - 1][x] == 0:
                y -= 1
            else:
                direction = 0
                x += 1

    return matrix


def print_spiral_square(matrix):
    for row in matrix:
        for num in row:
            print(num, end="\t")
        print()


def main():
    try:
        n = int(input("Ingrese un número para el tamaño del cuadrado en espiral: "))
        if n < 1:
            raise ValueError("El tamaño del cuadrado debe ser al menos 1")

        spiral_square = generate_spiral_square(n)
        print("\nCuadrado en espiral:")
        print_spiral_square(spiral_square)

    except ValueError as ve:
        print("Error:", ve)


if __name__ == "__main__":
    main()

