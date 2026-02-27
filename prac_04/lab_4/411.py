import json
import sys

def apply_patch(source, patch):
    for key, value in patch.items():
        if value is None:
            source.pop(key, None)
        elif key in source and isinstance(source[key], dict) and isinstance(value, dict):
            apply_patch(source[key], value)
        else:
            source[key] = value
    return source
source = json.loads(sys.stdin.readline())
patch = json.loads(sys.stdin.readline())
result = apply_patch(source, patch)
print(json.dumps(result, separators=(',', ':'), sort_keys=True))