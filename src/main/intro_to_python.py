def main():

    import numpy as np

    a = np.zeros( (3, 3) )


    print("Problem 1")

    for i in range(3):
        for j in range(3):
            if i == j:
                a[i][j] = 1
            else:
                a[i][j] = 0

    print(a)

    print("End of Problem 1")

    print("Problem 2")

    for i in range(3):
        for j in range(3):
            if i != j:
                a[i][j] = 3

    print(a)

    print("End of Problem 2")

    print("Problem 3")

    b = np.zeros( (3, 2) )

    for i in range(3):
        for j in range(2):
                b[i][j] = a[i][j]

    print(b)

    print("End of Problem 3")



if __name__ == "__main__":
    main()
