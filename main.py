from matplotlib import pyplot as plt

from calculations import akselerasjon, fart, magnetfelt, pos


def main():
    p = [0, 0, 0]
    B = [0, 0, 1e-3]
    v = [0, 3.58e4, 0]
    q = 1.67e-19
    m = 9.11e-31
    E = [-35.8, 0, 0]

    N = 10000
    T = 0.000000034
    dt = T/N

    x = []
    y = []
    z = []


    for i in range (N):
        if p[1] >= 0.0002:
            E = [0,0,0]
        B[2] = magnetfelt(p, False)
        a = akselerasjon(v, B, q, m, E)
        v = fart(a, v, dt)
        p = pos(v, p, dt)

        x.append(p[0])
        y.append(p[1])
        z.append(p[2])

    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.plot3D(x, y, z)
    ax.set_xlabel("X/m")
    ax.set_ylabel("Y/m")
    ax.set_zlabel("Z/m")
    ax.set_title("Partikkel i magnetfelt")
    plt.show()


if __name__ == "__main__":
    main()