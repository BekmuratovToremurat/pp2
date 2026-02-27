import json
import sys
import re

def resolve_path(data, query):
    tokens = re.findall(r'([a-zA-Z_]\w*|\[\d+\])', query)
    current = data

    for token in tokens:
        if token.startswith('[') and token.endswith(']'):
            try:
                idx = int(token[1:-1])
                current = current[idx]
            except (ValueError, IndexError, TypeError):
                return "NOT_FOUND"
        else:
            try:
                current = current[token]
            except (KeyError, TypeError):
                return "NOT_FOUND"
    return json.dumps(current, separators=(',', ':'))
data = json.loads(sys.stdin.readline())
q = int(sys.stdin.readline())

for _ in range(q):
    query = sys.stdin.readline().strip()
    print(resolve_path(data, query))