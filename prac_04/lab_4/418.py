x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

xr = x1 + y1 * (x2 - x1) / (y1 + y2)
yr = 0.0

print(f"{xr:.10f} {yr:.10f}")