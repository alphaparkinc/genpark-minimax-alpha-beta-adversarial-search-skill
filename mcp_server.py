"""MCP Server for Minimax Alpha-Beta Skill."""
import json
import sys
from client import MinimaxAlphaBeta

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "minimax_search",
                            "description": "Find optimal adversarial decision using Alpha-Beta pruning",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "game_tree": {"type": "object"},
                                    "depth": {"type": "integer"},
                                    "maximizing_player": {"type": "boolean"}
                                },
                                "required": ["game_tree", "depth"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                score, move = MinimaxAlphaBeta.search(
                    node=args["game_tree"],
                    depth=args["depth"],
                    alpha=float("-inf"),
                    beta=float("inf"),
                    maximizing_player=args.get("maximizing_player", True)
                )
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"best_move": move, "payoff_score": score})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
