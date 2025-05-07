from matplotlib import pyplot as plt

from calculations import fart, kraft, pos, magnetfelt


def main():
    p = [0, 0, 0]
    B = [0, 0, 1e-3]
    v = [0, 3.58e4, 0]
    q = 1.67e-19
    m = 9.11e-31

    N = 10000
    T = 0.0000001
    dt = T/N

    x = []
    y = []
    z = []


    for i in range (N):
        B[2] = magnetfelt(p)
        a = kraft(v, B, q, m)
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