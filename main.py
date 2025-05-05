def main():
    B = [0, 0, 1e-3]
    p = [0, 0, 0]
    v = [0, 3.58e4, 0]
    q = 1.67e-19
    m = 9.11e-31

    N = 100
    T = 0.00048
    dt = T/N

    x = []
    y = []
    z = []

    def kraft(v1, v2, q, m):
        x = v1[1] * v2[2] - v1[2] * v2[1]
        y = -(v1[0] * v2[2] - v1[2] * v2[0])
        z = v1[0] * v2[1] - v1[1] * v2[0]
        return [(q*x)/m, (q*y)/m, (q*z)/m]
    
    def fart(a, v, dt):
        vx = v[0] + a[0]*dt
        vy = v[1] + a[1]*dt
        vz = v[2] + a[2]*dt
        return [vx, vy, vz]
    
    def pos(v, p, dt):
        px = p[0] + v[0]*dt
        py = p[1] + v[1]*dt
        pz = p[2] + v[2]*dt
        return [px, py, pz]

    
    for i in range (N):
        a = kraft(v, B, q, m)
        v = fart(a, v, dt)
        p = pos(v, p, dt)


        

        x.append(p[0])
        y.append(p[1])
        z.append(p[2])
    
    print(x)
    print(y)
    print(z)


if __name__ == "__main__":
    main()