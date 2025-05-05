def main():
    B = [0, 0, 1]
    p = [0, 0, 0]
    v = [1, 0, 0]

    def vektorprodukt(v1, v2):
        x = v1[1] * v2[2] - v1[2] * v2[1]
        y = -(v1[0] * v2[2] - v1[2] * v2[0])
        z = v1[0] * v2[1] - v1[1] * v2[0]

if __name__ == "__main__":
    main()