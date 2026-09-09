import sys
import json
from client import StoerWagnerMinCut

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "min_cut":
        solver = StoerWagnerMinCut()
        return solver.find_min_cut(params.get("n", 3), params.get("matrix", []))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
