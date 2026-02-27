import json
import sys

def find_diffs(d1, d2, path=""):
    diffs = []
    keys = set(d1.keys()) | set(d2.keys())
    for key in keys:
        v1 = d1.get(key, "<missing>")
        v2 = d2.get(key, "<missing>")
        current_path = f"{path}.{key}" if path else key

        if isinstance(v1, dict) and isinstance(v2, dict):
            diffs.extend(find_diffs(v1, v2, current_path))
        elif v1 != v2:
            s1 = json.dumps(v1, separators=(',', ':')) if v1 != "<missing>" else "<missing>"
            s2 = json.dumps(v2, separators=(',', ':')) if v2 != "<missing>" else "<missing>"
            diffs.append(f"{current_path} : {s1} -> {s2}")
    return diffs
obj1 = json.loads(sys.stdin.readline())
obj2 = json.loads(sys.stdin.readline())
diffs = find_diffs(obj1, obj2)
if diffs:
    for line in sorted(diffs):
        print(line)
else:
    print("No differences")