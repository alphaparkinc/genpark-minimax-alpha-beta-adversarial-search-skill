"""Example usage for Minimax Alpha-Beta Skill."""
from client import MinimaxAlphaBeta

def main():
    print("Executing Minimax with Alpha-Beta Pruning...")
    game_tree = {
        "children": {
            "ACTION_A": {
                "children": {
                    "A1": {"value": 3.0},
                    "A2": {"value": 5.0}
                }
            },
            "ACTION_B": {
                "children": {
                    "B1": {"value": 7.0},
                    "B2": {"value": 8.0}
                }
            }
        }
    }
    score, best_move = MinimaxAlphaBeta.search(game_tree, depth=2, alpha=float("-inf"), beta=float("inf"), maximizing_player=True)
    print(f"Optimal move: {best_move} with guaranteed payoff: {score}")
    assert best_move == "ACTION_B", f"Expected ACTION_B, got {best_move}"
    assert score == 7.0
    print("Minimax Alpha-Beta verified successfully!")

if __name__ == "__main__":
    main()
