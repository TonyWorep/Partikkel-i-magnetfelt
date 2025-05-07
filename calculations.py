from math import e

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

def magnetfelt(p):
    return (1e-3)/e**(p[1]*2000)

def main():
    print("Wrong here bud.")

if __name__ == "__main__":
    main()