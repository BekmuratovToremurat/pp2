import math

def solve_circle_path():
    R = float(input().strip())
    x1, y1 = map(float, input().strip().split())
    x2, y2 = map(float, input().strip().split())
    
    OA = math.sqrt(x1*x1 + y1*y1)
    OB = math.sqrt(x2*x2 + y2*y2)
    AB = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    if OA < R or OB < R:
        OA = max(OA, R)
        OB = max(OB, R)
    
    alpha = math.acos(R / OA) if OA > R else 0
    beta = math.acos(R / OB) if OB > R else 0
    
    cos_gamma = (OA*OA + OB*OB - AB*AB) / (2 * OA * OB)
    cos_gamma = max(-1.0, min(1.0, cos_gamma))
    gamma = math.acos(cos_gamma)
    
    if gamma <= alpha + beta + 1e-12:
        print(f"{AB:.10f}")
    else:
        tangent1 = math.sqrt(OA*OA - R*R) if OA > R else 0
        tangent2 = math.sqrt(OB*OB - R*R) if OB > R else 0
        arc_length = R * (gamma - alpha - beta)
        total = tangent1 + tangent2 + arc_length
        print(f"{total:.10f}")

if __name__ == "__main__":
    solve_circle_path()