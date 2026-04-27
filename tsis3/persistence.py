import json
import os

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {"sound": True, "car_color": "red", "difficulty": "normal"}

    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)


def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_score(name, score, distance):
    board = load_leaderboard()
    board.append({"name": name, "score": score, "distance": distance})
    board = sorted(board, key=lambda x: x["score"], reverse=True)[:10]
    save_leaderboard(board)