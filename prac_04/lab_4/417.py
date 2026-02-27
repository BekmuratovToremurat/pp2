import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

seg_len = math.hypot(dx, dy)

if seg_len == 0:
    if x1*x1 + y1*y1 <= R*R:
        print(f"{0.0:.10f}")
    else:
        print(f"{0.0:.10f}")
    exit()

ux = dx / seg_len
uy = dy / seg_len

a = dx*dx + dy*dy
b = 2*(x1*dx + y1*dy)
c = x1*x1 + y1*y1 - R*R

discriminant = b*b - 4*a*c

if discriminant < -1e-10:
    print(f"{0.0:.10f}")
else:
    t1 = t2 = 0
    if discriminant < 0:
        discriminant = 0.0
    sqrt_disc = math.sqrt(discriminant)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    t_start = max(0, min(t1, t2))
    t_end = min(1, max(t1, t2))
    if t_start > t_end:
        print(f"{0.0:.10f}")
    else:
        length_inside = seg_len * (t_end - t_start)
        print(f"{length_inside:.10f}")