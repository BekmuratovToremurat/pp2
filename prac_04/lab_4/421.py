import importlib
import sys

def solve_module_query():
    q = int(input().strip())
    
    for _ in range(q):
        line = input().strip()
        parts = line.split()
        if len(parts) == 2:
            module_path, attr_name = parts
        else:
            continue
        
        try:
            module = importlib.import_module(module_path)
            
            if hasattr(module, attr_name):
                attr = getattr(module, attr_name)
                if callable(attr):
                    print("CALLABLE")
                else:
                    print("VALUE")
            else:
                print("ATTRIBUTE_NOT_FOUND")
                
        except ModuleNotFoundError:
            print("MODULE_NOT_FOUND")
        except ImportError:
            print("MODULE_NOT_FOUND")
        except Exception as e:
            print("MODULE_NOT_FOUND")

if __name__ == "__main__":
    solve_module_query()