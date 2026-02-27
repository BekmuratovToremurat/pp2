def solve_scope_accumulator():
    m = int(input().strip())
    
    g = 0 
    n = 0 
    
    for _ in range(m):
        scope, value_str = input().strip().split()
        value = int(value_str)
        
        if scope == "global":
            g += value
        elif scope == "nonlocal":
            n += value
        elif scope == "local":
            pass
    
    print(g, n)

if __name__ == "__main__":
    solve_scope_accumulator()